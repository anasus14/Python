function calcularDiferencia() {
  var fecha1 = obtenerFecha(document.getElementById("fecha1").value);
  var fecha2 = obtenerFecha(document.getElementById("fecha2").value);

  // Verificar que las fechas sean válidas
  if (!fecha1 || !fecha2) {
    alert("Por favor, ingrese fechas válidas en formato dd/mm/yyyy.");
    return;
  }

  // Verificar que la fecha 2 sea mayor o igual que la fecha 1
  if (fecha2 < fecha1) {
    alert("La fecha 2 debe ser mayor o igual que la fecha 1.");
    return;
  }

  // Calcular la diferencia en días, meses y años
  var diferencia = fecha2 - fecha1;

  var unDia = 1000 * 60 * 60 * 24;
  var años = Math.floor(diferencia / (unDia * 365));
  var meses = calcularMesesTranscurridos(fecha1, fecha2);
  var días = Math.floor(diferencia / unDia);

  // Mostrar el resultado
  document.getElementById("resultado").innerHTML = "Días: " + días + ", Meses: " + meses + ", Años: " + años;
}

function obtenerFecha(fechaString) {
  var partes = fechaString.split('/');
  if (partes.length !== 3) {
    return null;
  }
  var día = parseInt(partes[0], 10);
  var mes = parseInt(partes[1], 10) - 1; // Restar 1 porque los meses en JavaScript son base 0
  var año = parseInt(partes[2], 10);

  // Verificar que el año esté dentro del rango de 1900 a 2099
  if (año < 1900 || año > 2099) {
    return null;
  }

  return new Date(año, mes, día);
}

function calcularMesesTranscurridos(fecha1, fecha2) {
  var meses = (fecha2.getFullYear() - fecha1.getFullYear()) * 12;
  meses -= fecha1.getMonth();
  meses += fecha2.getMonth();

  // Si la fecha2 tiene un día menor que la fecha1, restamos un mes
  if (fecha2.getDate() < fecha1.getDate()) {
    meses--;
  }

  return meses;
}
function agregarSeparadores(inputId) {
  var input = document.getElementById(inputId);
  var fecha = input.value;
  var separador = "/";

  if (fecha.length === 2 || fecha.length === 5) {
    fecha += separador;
  }

  input.value = fecha;
}