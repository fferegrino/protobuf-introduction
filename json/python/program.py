import dataclasses
import json

@dataclasses.dataclass
class Contacto:
    nombre: str
    telefono: str


def main():
    contacto = Contacto(
        nombre="Masiosare", 
        telefono="55 5658 1111"
    )
    
    with open("contacto.json", "w") as writable:
        json.dump(dataclasses.asdict(contacto), writable)



if __name__ == "__main__":
    main()