$(document).ready(function () {

    var table = $('#tabela-listar').DataTable({
        responsive: true,
        // "bSort": false,
        "aaSorting": [],
        "pageLength": 50,
        "language": {
            "decimal": "",
            "emptyTable": "Sem dados disponíeis",
            "info": "Mostrando de _START_ até _END_ de _TOTAL_ registos",
            "infoEmpty": "Mostrando de 0 até 0 de 0 registos",
            "infoFiltered": "(filtrado de _MAX_ registos no total)",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "Mostrar _MENU_ registos",
            "loadingRecords": "A carregar dados...",
            "processing": "A processar...",
            "search": "Procurar:",
            "zeroRecords": "Não foram encontrados resultados",
            "paginate": {
                "first": "Primeiro",
                "last": "Último",
                "next": "Seguinte",
                "previous": "Anterior"
            },
            "aria": {
                "sortAscending": ": ordem crescente",
                "sortDescending": ": ordem decrescente"
            }
        }
    });

    new $.fn.dataTable.FixedHeader(table);
});