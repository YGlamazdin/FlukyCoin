import base64

from crypto.xmss import *

if __name__ == '__main__':
    # Пример использования

    # print(len(str("""00000083169139f9b3780247f77706a19fbd504e77bda1fd269e0a813e1528f18413dbcd195d8b00f9057c5972f3f7e179652828203c13488e4f4ae8f7d738685972a135cdb4c1b17f6ad28ce5f63184088a81b7e906637c5c6e1a2f89cd8e371c2cdcc1561ee77269adf0c719ff83235eb5cc57b8a90f08a239f8c12845d1a9161e5dd68f5d802491e0b9d574d6c9abd61d75ac6f4418db19f31653d7bf0ad3f0a979943b4c505bfc819aed22a1c6e2ab1fb8aaf1e9caa7746158411d8daa1d4852b59198dec92bed79b3e6905b8103b140b7efae49ea193ec75aa3b77fa6cb189380f8604c94f27db0fdb0864c50aa29c0077acb255b4f3b1963cf3ddb570df2d00e57d303ae887493a3cd840f6bc3c01b6e047ed398a17fc1550d45b2c9f70a861461a6097bb0d7653e60a8897304b73c6124fcf2545d1abe146f8be755aa9b8f9208c7e772f3f207af030e144f32c53966a0646ec4a53cf605dcb4a5efdc3869de1ec138fba1061f551bca434b64cacf16ae77fe817e432cff2ffd10c430a5069f520d65b2321a2e065c1e92387601f123b745b5eaeb1698e1560654800fe61020b930a800ca5c6fdbbfce9433c10471ec09fe7a6a4b70a2185b61b025d783bcee452114cc70df15bf75d6a35b716b36fa6152a17a3d987e2ca42cd10429e010a0f10e95d0833d238410f6a7eb56dbc3a8dbfaa6e2159c839dc0db8942fdaa793c104ebfc0c60bd1939ac4282b3a142d5a62af4bcba8a0b20de9b325feb4e9795c1df7a0a0f402630239c52f84386d7e1a32374577c8fe266f174ac0e2307201a1f7a6398fe1efbf4f231c461cc0a90fcc64e6426f342bc85df377d1436ef3cf8928a6a005cde200bdafea8c612a2d9bad9380e2d31928e59ed17704f1f9f22255fc00e95b24a2204e2b67f193961c4d1fadf364af9763cbd8868d211fb62290243fd4e081b21dbfe9b4295ea8576fa8441153ee0d97be4d38209f03cd40fedd12a32aac575a190976252cba87c83ff66f86e76b728235a5adc84f3368cded7f30e4f34731cb9cf175b784de672c8d76d4dbbb0f2165163a5eda35ffcf22410c3cd920acb36cf8f7dc6025f8a1c5545a5bb82f2fedefc01183433073e478e08228883b3ebaf1e7cdc5e3a048857c4728aaa48b22e7fdd1cdb1b30fdefb7ed569b21ed31ca41798409aeac1ead3bb0a5c341fa3765de7a78180e2c598f9cf5328d4e1b53528dcbed3d7df4637beda663f5b8ffd54417562ac5645e6da5bcff081fbc5f0254bffe2c23213244371d464cc39e4452f9c03686a622ef5df8677c4ec000afc91e7ff530c598e9e366a612c2f48d2cc1c3354ff40568e19204e59d6278739819cb556a396f4625e4a828446e932c775f78e7101b72b61f3963353c69d296dc9269aaa52f6e13729d29a59d2985f8ae1b06aa94dd44c0d8bd80608d733450557ef514573b7ae72962c710cab64800de9526140b939a0c5b418fc6c5e4844c1582fd796dc4134da98f0b235cbb32846c13ad1705eba4700aa576506ee2a7a8a67b6ed7b17c1b71bcd02e50012fce5e332a54ea5009802d6477a81afb646c1fa4b9da0238f6110529db03cc5e74ce680fa694dbf510802d2b4955498a9e04a7eef3458a5890103c37e33323a502c6574bec1fe5abf560e8833efffb4a0d3d72b4dfa74a6a8d50ab574c88b090037d795e4f01619f0cec601e5a97429e6cdf52dfd8ad2696c82a89604cd25bff9aeeee03a5fcdae02cafe757016ec2f83ad373d98673011060e96e37d441b4571cb8427d32f89a43cf0547a27aa3770b08dc2f87711bf31dcc352b968873a797e1e2d357981cfc511897ee6f3c3b206b076d127a1a11aed3584f3ac1d1ad93b8fc526332d60d4054012f0d202ad1745562801ea5318b285d72f07fd8b3a0a65709aed5885b31c046d42b01e3abdfc3755baaaf22a6484233c2316a22113d72faf18263cc7761b63be70f93b9c201776ecfb2842a35d851f9d6ca3cbbfdd3f2881497f536f48c6cb6548444f1f1545ed9814cbd908b0d433cda491a551889d3f2bec516eebc30d7a302373759697289c28bb49f0d401796a9b8f420d86b2cbcaf57f6d0141161ae394fb93139016d38727293f47795a34bcdd2164d953b48ca68b927a90a19342aca443cdb9272397384255bff92a66b0da14934eb7e9620ced75d53b13b5d280e0a18397587711caa9ab8cc1ef88faa3b18473f9bf29231415fe404954d3577b625f645f6be9e6b34afa52b0e66eface378b810f2dd5124529c722d2ad0d49aab21b7ad27648c17b8086030715ed8a5714897c6ae26802e3ed738b3d7870508e3e78f8508c439873094f11178268d6b6d72f94ba76c3061c562e3de1ce8cd3766405e3c0e1b32bd6f3953a9f764c6fd3e880fb55156d21c903ff30c28f6da13bec24701adf0c3fe2d7af2c0db4384dc248556c66b5bb13f219b5ce4e298ddbcd3ec70cd8f2c31c63242fb3b2d7b08bb25fa43ad63fef5458b9c8395cbb5f8e33b0efa95d84275124c076dd815aa7aa91578ad69293e852c8f4eb10c3a166db83aff369e0a7aa6029835ee2f81177598184b37e3d697a7ca742039ffebdf271560fb31059dffe576f13ff392f0be136040ce674ac6f0855a73b7c556f56cb4e2943a51ad126be46af47ca2660ee16e37cf3863e3f8098e83ee09c3cfd0407f790a44932d36d42112f3e6579bc859786d14207697cdf0af6f1884a3afc1f5853d0cd09c59fa5a88700483f2fa62566ba31a247f9e7986065a8d65ae69b4bdb6bdac22d66cf82f067fd427e1bf6483916c5d25911ecc909f14d8e669401a6a71fcfc4e5cf912310b96679a82e5c0af2079365adb336ae5277c36c742045b366d8c9902dcf4fa60f5844d00457dea26fff79b95f875d0fbe2bc2c3c4e1e3673f7b79a8a779b4e6ee9892a4f1544549684f3094c7da4bf7b639f919415345e07df70aee76cee891e3b93a2f02fedc8cd55b91c48bea7b4c5701081f5fcf2c4c6e9d7b4ce4acb162312ac054373039c468ed112d48b155a5e75ae82ee3b5150067ccfc88fa8004203e3b214f387a133d52c60707bd882e6ff1bc4bea7587af1870937a3b2bd0a89fe0c23a2655f371644cd47300862781afb39f2feb117cd31cb6f6239acb3bed4384ec81aac5cb3bf01d208612baca2d436bf6badd8ab7d375ae5d39e06b98018dd0b4adec122f7873be12ac6846f2674df7b5511e655b8bf4509d34b01d1a18eedd9ea9abe351d76522822d95210570253f23f27ce7e71a0087c9b319be7892a0ab2e914a7f862641e72624a62bb7a308dd5a5bd257bf560e8e4bec94248b3448b232194e342cd4dedd88e9718727b40235cf151cca02c465960521d11d37812b177132d9672e91fbeb6336d02d91f6df89acd3577046f8b85b78dc2af62fddea6569b87ab9c4e4fe25d5307bf8a505a50d64efa81ba6ae9c07a67cf149f5f1ecf3924c7f1ae4d147304b52e00695b96693999c4ecdbfc1378dce3a3da386b160ba61ce0931f9e796d92675d17f59f3b7ad242cdd29e6a732045f221e61f4fc9090059dffcffc053ba51b0824bd3a2e5e45f617fadec97dccef6abda4a0b7dcff1a6d04034dc96768""")))

    keys = XMSS.create(5)
    private = keys.private_key.hex()
    print("private key", keys.private_key.hex())
    print("seed_phrase", keys.seed_phrase)
    message = b"123"
    signature = keys.sign(message=message)
    # print(len(sign.to_str()))
    # print(sign.to_str())

    print("Address s_valid", keys.keyPair.PK.is_valid_address(keys.address))

    pk_str = keys.keyPair.PK.to_hex()

    # публичный ключ из строки
    PK = XMSSPublicKey.from_hex(pk_str)
    verification_result = PK.verify_sign(signature.to_base64(), message=message)
    print(f"Результат верификации подписи: {'Подпись верна' if verification_result else 'Подпись неверна'}")

    keys2 = XMSS.create(key=private)
    print(keys2.address)
    print("seed_phrase", keys2.seed_phrase)
    print("private key", keys2.private_key.hex())

    '453952263c8ffc8f7ed251b7cbce2e53116a643cb3bff99554d975a2e6803d04c51ec16e'


    seed_phrase = keys2.seed_phrase

    keys3 = XMSS.create(seed_phrase=seed_phrase)
    print(keys3.address)
    print("seed_phrase", keys3.seed_phrase)
    print("private key", keys3.private_key.hex())
