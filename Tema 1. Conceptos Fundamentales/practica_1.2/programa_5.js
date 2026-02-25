//  5) Un programa que ejemplifique las características del paradigma asignado.

// Clase base - representa abstraccion de un vehiculo
class Vehiculo {
  // Atributo privado - encapsulacion
  #velocidad;

  constructor(marca, modelo) {
    this.marca = marca;
    this.modelo = modelo;
    this.#velocidad = 0;
  }

  // Metodo para aumentar velocidad
  acelerar(valor) {
    this.#velocidad += valor;
  }

  // Getter de velocidad
  getVelocidad() {
    return this.#velocidad;
  }

  // Setter con validacion
  setVelocidad(valor) {
    if (valor >= 0) {
      this.#velocidad = valor;
    }
  }

  // Metodo que sera sobreescrito (polimorfismo)
  descripcion() {
    return "Vehiculo generico";
  }
}

// Herencia - Auto extiende Vehiculo
class Auto extends Vehiculo {
  constructor(marca, modelo, puertas) {
    super(marca, modelo);
    this.puertas = puertas;
  }

  // Polimorfismo - sobreescribe descripcion()
  descripcion() {
    return `Auto: ${this.marca} ${this.modelo} - ${this.puertas} puertas`;
  }
}

// Herencia - Moto extiende Vehiculo
class Moto extends Vehiculo {
  constructor(marca, modelo, cilindrada) {
    super(marca, modelo);
    this.cilindrada = cilindrada;
  }

  // Polimorfismo - sobreescribe descripcion()
  descripcion() {
    return `Moto: ${this.marca} ${this.modelo} - ${this.cilindrada}cc`;
  }
}

// Crear objetos
const auto1 = new Auto("Toyota", "Corolla", 4);
const moto1 = new Moto("Yamaha", "R3", 300);

// Usar setter y acelerar
auto1.setVelocidad(60);
auto1.acelerar(20);

moto1.setVelocidad(90);
moto1.acelerar(10);

// Mostrar resultados - polimorfismo en accion
console.log(auto1.descripcion());
console.log("Velocidad auto: " + auto1.getVelocidad() + " km/h");

console.log(moto1.descripcion());
console.log("Velocidad moto: " + moto1.getVelocidad() + " km/h");
