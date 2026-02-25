// 2.Un programa que use funciones o métodos propios de su biblioteca.

// Clase que encapsula operaciones sobre una lista de numeros
class ListaNumeros {
  constructor(numeros) {
    this.numeros = numeros;
  }

  // Usa el metodo nativo filter() de Array
  mayoresQue(limite) {
    return this.numeros.filter((n) => n > limite);
  }

  // Usa el metodo nativo map() de Array
  duplicar() {
    return this.numeros.map((n) => n * 2);
  }

  // Usa el metodo nativo reduce() de Array
  sumaTotal() {
    return this.numeros.reduce((acc, n) => acc + n, 0);
  }
}

// Crear objeto y usar metodos nativos de la biblioteca
const lista = new ListaNumeros([2, 8, 4, 10, 3, 7]);

console.log("Numeros mayores que 5:", lista.mayoresQue(5));
console.log("Numeros duplicados:", lista.duplicar());
console.log("Suma total:", lista.sumaTotal());
