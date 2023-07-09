function calcularDiferencia() {
    var date1String = document.getElementById('date1').value;
    var date2String = document.getElementById('date2').value;
  
    var date1 = parseDate(date1String);
    var date2 = parseDate(date2String);
  
    if (date1 && date2) {
      var diff = date2.getTime() - date1.getTime();
  
      if (diff >= 0) {
        var days = Math.floor(diff / (1000 * 60 * 60 * 24));
        var months = Math.floor(days / 30.436875); // Average number of days in a month
        var years = Math.floor(months / 12);
  
        days = days % 30.436875; // Remaining days after calculating months
        months = months % 12; // Remaining months after calculating years
  
        var resultado = years + ' años, ' + months + ' meses, ' + days + ' días.';
        document.getElementById('resultado').textContent = resultado;
      } else {
        document.getElementById('resultado').textContent = 'La segunda fecha debe ser posterior a la primera fecha.';
      }
    } else {
      document.getElementById('resultado').textContent = 'Ingrese fechas válidas en el formato dd/mm/yyyy.';
    }
  }
  
  function parseDate(dateString) {
    var parts = dateString.split('/');
    var day = parseInt(parts[0], 10);
    var month = parseInt(parts[1], 10) - 1; // Months are zero-based
    var year = parseInt(parts[2], 10);
  
    if (isValidDate(day, month, year)) {
      return new Date(year, month, day);
    } else {
      return null;
    }
  }
  
  function isValidDate(day, month, year) {
    var date = new Date(year, month, day);
    return (
      date.getFullYear() === year &&
      date.getMonth() === month &&
      date.getDate() === day
    );
  }
  