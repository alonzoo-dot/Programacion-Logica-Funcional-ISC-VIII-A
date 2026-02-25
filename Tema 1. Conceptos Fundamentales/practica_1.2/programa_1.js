//1) Un programa que únicamente imprima texto.

// Clase que representa informacion del paradigma
class Paradigma {
  constructor(nombre, lenguaje) {
    this.nombre = nombre;
    this.lenguaje = lenguaje;
  }

  // Metodo que imprime la informacion
  imprimir() {
    console.log("Paradigma: " + this.nombre);
    console.log("Lenguaje seleccionado: " + this.lenguaje);
  }
}

// Crear objeto e imprimir
const p = new Paradigma("Orientado a Objetos", "JavaScript");
p.imprimir();
