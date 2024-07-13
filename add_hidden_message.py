from stegano import lsb
secret=lsb.hide("new.png","75c6be3e65d3ea4589efe6ce6e74e2c60d8ace83b3ce476dca311aa1908dca916")
secret.save("final1.png")
