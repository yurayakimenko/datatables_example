// Объявляем один раз базовый url
var base_url = "/mydata";

// Пытаюсь найти ошибку
var table = $('#mytable').DataTable({
        ajax: get_url(),
        responsive: true,
        columns: [
            { data: 'id' },
            { data: 'area' },
            { data: 'price' },
            { data: 'currency' },
            { data: 'description' }
        ],
        columnDefs: [{
            "targets": 0,
            "orderable": false
        }]
    }
);

// Генерация url для запроса
function get_url() {
    var period = $("#period_select").val();
    var url;
    if (period == 'day') {
        unit = 'hour';
        tooltipFormat = 'HH:mm DD.MM.YYYY';
        $("#date_calendar").insertBefore("#date_range");
        $("#date_calendar").show();
        $("#date_range").hide();
        url = base_url+"?period=" + $("#date").val();
    }
    else if (period == 'date_range') {
        unit = 'hour';
        tooltipFormat = 'HH:mm DD.MM.YYYY';
        $("#date_range").insertBefore("#date_calendar");
        $("#date_calendar").hide();
        $("#date_range").show();
        url = base_url+"?period=" + $("#start").val() + "_" + $("#end").val();
    }
    else if (period == 'hour') {
        unit = 'minute';
        tooltipFormat = 'HH:mm DD.MM.YYYY';
        $("#date_calendar").hide();
        $("#date_range").hide();
        url = base_url+"?period=hour";
    }
    else if (period == '15min' || period == '30min') {
        unit = 'minute';
        tooltipFormat = 'HH:mm DD.MM.YYYY';
        $("#date_calendar").hide();
        $("#date_range").hide();
        url = base_url+"?period=" + period;
    }
    else {
        unit = 'day';
        tooltipFormat = 'DD.MM.YYYY';
        $("#date_calendar").hide();
        $("#date_range").hide();
        url = base_url+"?period=" + period;
    }
    return url;
}

// Функция запроса данных (делаем подмену url-а для запроса таблицей и инициируем повторний запрос таблицы)
// Вся инфа есть, если загуглить DataTables доки
function refresh_ajax() {
    table.ajax.url(get_url()).load();
};

// Инициализация datepicker-ов
$('#date').datepicker({
    format: "dd/mm/yyyy",
    maxViewMode: 2,
    language: "ru",
    orientation: "bottom right"
});

$('.input-daterange').datepicker({
    format: "dd/mm/yyyy",
    maxViewMode: 2,
    language: "ru",
    orientation: "bottom right"
});
// -----------

$(document).ready(function () {
    // Делаем привязку смены параметров даты к функции, которая делат изменённый запрос к бэкенду
    $("#period_select").on("change", refresh_ajax);
    $("#date").on("change", refresh_ajax);
    $("#start").on("change", refresh_ajax);
    $("#end").on("change", refresh_ajax);
    $("#currency_select").on("change", refresh_ajax);
});