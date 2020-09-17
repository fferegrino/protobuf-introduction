from contacto_pb2 import Contacto


def main():
    contacto = Contacto(
        nombre="Masiosare", 
        telefono="55 5658 1111"
    )
    

    with open("contacto.protobuf", "wb") as writable:
        writable.write(contacto.SerializeToString())



if __name__ == "__main__":
    main()