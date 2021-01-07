//Pruebas de Formulas mátemáticas sencillas del tipo c = a op b
c = b + 5;
cont = cont + 1;
resultado = 12.7 + 3.14;

//Pruebas de Formulas más complejas del tipo c = a op ( b op d) 
y = 9  *  (2 + x);
resultado = (a - 5) / 2;

//Pruebas de expresiones con estructuras de control

//Ejemplo de for
for (var i = 0; i < 9; i++) {
   n += i;
   mifuncion(n);
}

// Ejemplo de While
n = 0;
x = 0;
while (n < 3) {
  n ++;
  x += n;
}

// Ejemplo de Switch Case
switch (expr) {
  case 'Naranjas':
    console.log('El kilogramo de naranjas cuesta $0.59.');
    break;
  case 'Manzanas':
    console.log('El kilogramo de manzanas cuesta $0.32.');
    break;
  case 'Platanos':
    console.log('El kilogramo de platanos cuesta $0.48.');
    break;
  case 'Cerezas':
    console.log('El kilogramo de cerezas cuesta $3.00.');
    break;
  case 'Mangos':
  case 'Papayas':
    console.log('El kilogramo de mangos y papayas cuesta $2.79.');
    break;
  default:
    console.log('Lo lamentamos, por el momento no disponemos de ' + expr + '.');
}
console.log("¿Hay algo más que te quisiera consultar?");

//Ejemplo de If
if (cipher_char == from_char) {
   result = result + to_char;
   x++;
} else
   result = result + clear_char;