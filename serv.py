import obj
import Pyro5
from crud import Personagens

def main():
    daemon = Pyro5.server.Daemon()
    uri = daemon.register(Personagens)
    print("Objeto servidor publicado.")
    print("URI do objeto: ", uri)

    ns= Pyro5.core.locate_ns()
    ns.register("carlosdreyer", uri)
    seria = Pyro5.serializers.SerializerBase()
    seria.register_class_to_dict(obj.chara, obj.chara_class_to_dict)
    input("parada um")
    daemon.requestLoop()

if __name__ == "__main__":
    main()
