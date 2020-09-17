using System.IO;
using Newtonsoft.Json;

namespace Agenda
{
    class Contacto 
    {
        [JsonProperty("nombre")]
        public string Nombre { get; set; }

        [JsonProperty("telefono")]
        public string Telefono { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var contacto = new Contacto
            {
                Nombre = "Masiosare",
                Telefono = "55 5658 1111"
            };

            JsonSerializer serializer = new JsonSerializer();

            using (StreamWriter sw = new StreamWriter(@"contacto.json"))
            using (JsonWriter writer = new JsonTextWriter(sw))
                serializer.Serialize(writer, contacto);
        }
    }
}
