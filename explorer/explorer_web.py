import grpc
from flask import Flask, request, render_template_string
from protos import network_pb2, network_pb2_grpc
from wallet_app.Wallet import Wallet  # Убедитесь, что путь импорта корректен
from datetime import datetime

app = Flask(__name__)
wallet = Wallet()  # Инициализируйте ваш кошелек здесь

def parse_node_info(response):
    """ Преобразование ответа gRPC в словарь """
    last_block_time = response.last_block_time
    if last_block_time:
        last_block_time = datetime.fromtimestamp(last_block_time).strftime("%Y-%m-%d %H:%M:%S")
    else:
        last_block_time = "N/A"

    return {
        "synced": response.synced,
        "blocks": response.blocks,
        "peers": list(response.peers),
        "peer_count": len(response.peers),
        "last_block_time": last_block_time
    }

def get_info(server="192.168.0.26:9334"):
    """ Информация с ноды """
    # Создание канала связи с сервером
    channel = grpc.insecure_channel(server)
    stub = network_pb2_grpc.NetworkServiceStub(channel)

    # Запрос на получение информации о сети
    net_info_request = network_pb2.Empty()

    try:
        # Отправка запроса и получение ответа
        response = stub.GetNetInfo(net_info_request)
        return parse_node_info(response)

    except grpc.RpcError as e:
        print(f"Ошибка gRPC: {str(e)}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    node_info = get_info()

    if node_info is None:
        return "Ошибка получения информации о ноде"

    if request.method == 'POST':
        address = request.form['address']
        try:
            info = wallet.info(address)  # Метод info должен возвращать объект с атрибутом balance
            balance = info.balance / 10000000  # Предполагаем, что баланс нужно сконвертировать
            return render_template_string('''
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Wallet Balance</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                        }
                        .balance-info {
                            font-size: 1.2em;
                            margin-top: 20px;
                        }
                        .address {
                            font-weight: bold;
                        }
                        .balance {
                            color: green;
                        }
                    </style>
                </head>
                <body>
                    <h1>Node Information</h1>
                    <p><strong>Synced:</strong> {{ node_info.synced }}</p>
                    <p><strong>Blocks:</strong> {{ node_info.blocks }}</p>
                    <p><strong>Peers ({{ node_info.peer_count }}):</strong></p>
                    <ul>
                        {% for peer in node_info.peers %}
                        <li>{{ peer }}</li>
                        {% endfor %}
                    </ul>
                    <p><strong>Last Block Time:</strong> {{ node_info.last_block_time }}</p>
                    <div class="balance-info">
                        <p class="address">Balance for address {{ address }}:</p>
                        <p class="balance">{{ balance }}</p>
                    </div>
                    <a href="/">Check another address</a>
                </body>
                </html>
            ''', address=address, balance=balance, node_info=node_info)
        except Exception as e:
            return f"An error occurred: {str(e)}"

    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Wallet Balance</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                }
                .balance-info {
                    font-size: 1.2em;
                    margin-top: 20px;
                }
                .address {
                    font-weight: bold;
                }
                .balance {
                    color: green;
                }
            </style>
        </head>
        <body>
            <h1>Node Information</h1>
            <p><strong>Synced:</strong> {{ node_info.synced }}</p>
            <p><strong>Blocks:</strong> {{ node_info.blocks }}</p>
            <p><strong>Peers ({{ node_info.peer_count }}):</strong></p>
            <ul>
                {% for peer in node_info.peers %}
                <li>{{ peer }}</li>
                {% endfor %}
            </ul>
            <p><strong>Last Block Time:</strong> {{ node_info.last_block_time }}</p>
            <h1>Enter Wallet Address</h1>
            <form method="post">
                <input type="text" name="address" placeholder="Enter wallet address" required>
                <input type="submit" value="Get Balance">
            </form>
        </body>
        </html>
    ''', node_info=node_info)

if __name__ == '__main__':
    app.run(debug=True, port = 80)