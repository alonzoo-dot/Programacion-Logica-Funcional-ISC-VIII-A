// 4.U.n programa que concantene cadenas, variables y/o valores numéricos.

// Clase Persona con metodo que concatena datos
class Persona {
  constructor(nombre, edad, ciudad) {
    this.nombre = nombre;
    this.edad = edad;
    this.ciudad = ciudad;
  }

  // Metodo que concatena con template literals y con operador +
  presentarse() {
    // Concatenacion con template literals
    console.log(
      `Hola, me llamo ${this.nombre}, tengo ${this.edad} anos y vivo en ${this.ciudad}.`,
    );

    // Concatenacion con operador + (tradicional)
    console.log(
      "En 5 anos, " + this.nombre + " tendra " + (this.edad + 5) + " anos.",
    );
  }
}

// Crear objeto y llamar metodo
const persona = new Persona("Carlos", 20, "Chetumal");
persona.presentarse();
