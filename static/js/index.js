var table = $('#mytable').DataTable( {
    ajax: {
        url: '/mydata',
        type: "POST",
        dataSrc: '',
        data: function (d) {
            d.mode = $("#datepicker").val()
        }
    },
    columns: [
        { data: 'id' },
        { data: 'area' },
        { data: 'price' },
        { data: 'currency' },
        { data: 'description' }
    ]
});

function datepicker_change () {
    table.ajax.reload();
};