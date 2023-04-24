const c1 = document.getElementById('myChart1');

  new Chart(c1, {
    type: 'bar',
    data: {
      labels: ['Jan', 'Feb', 'March', 'April', 'May', 'June','July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      datasets: [{
        label: 'Revenue',
        data: [12, 9, 5, 10, 7,12, 9, 5, 10, 7,4,15],
        borderWidth: 1,
        backgroundColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          
        ],
      }]
    },
    options: {
      maintainAspectRatio:false,
    }
  });





const ctx = document.getElementById('myChart2');

  new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Syrups', 'Injections', 'Pills', 'Capsules', 'Drops', 'Solutions'],
      datasets: [{
        label: 'Medicines Type',
        data: [12, 9, 5, 10, 7],
        borderWidth: 1,
        backgroundColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
        ],
      }]
    },
    options: {
      maintainAspectRatio:false,
    }
  });


