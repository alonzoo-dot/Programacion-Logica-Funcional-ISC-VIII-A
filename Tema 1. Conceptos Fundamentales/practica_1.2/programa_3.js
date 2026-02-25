//3.Un programa que implemente estructuras de control de flujo para toma de decisiones.

// Clase Estudiante con estructura de decision
class Estudiante {
  constructor(nombre, calificacion) {
    this.nombre = nombre;
    this.calificacion = calificacion;
  }

  // Metodo que evalua la calificacion con if/else
  evaluar() {
    if (this.calificacion >= 90) {
      console.log(this.nombre + " obtuvo una A - Excelente!");
    } else if (this.calificacion >= 80) {
      console.log(this.nombre + " obtuvo una B - Bien hecho");
    } else if (this.calificacion >= 70) {
      console.log(this.nombre + " obtuvo una C - Aceptable");
    } else {
      console.log(this.nombre + " necesita mejorar");
    }
  }
}

// Crear objetos y evaluar
const estudiante1 = new Estudiante("Ana", 95);
const estudiante2 = new Estudiante("Luis", 78);
const estudiante3 = new Estudiante("Marta", 55);

estudiante1.evaluar();
estudiante2.evaluar();
estudiante3.evaluar();
