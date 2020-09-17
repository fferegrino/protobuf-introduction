using System.IO;
using Google.Protobuf;

namespace Agenda
{

    class Program
    {
        static void Main(string[] args)
        {
            var contacto = new Contacto
            {
                Nombre = "Masiosare",
                Telefono = "55 5658 1111"
            };

            using (var output = File.Create(@"contacto.protobuf"))
                contacto.WriteTo(output);
        }
    }
}
