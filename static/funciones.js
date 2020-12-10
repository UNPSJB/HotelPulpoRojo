let get_calendar = (calendar_selector, start_calendar=null, end_calendar=null) => {
    
    $(calendar_selector).calendar({
        type: 'date',
        monthFirst: false,
        startCalendar: start_calendar,
        endCalendar: end_calendar || null,
        text: {
                days: ['D', 'L', 'M', 'X', 'J', 'V', 'S'],
                months: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
                monthsShort: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
                today: 'Hoy',
                now: 'Ahora',
                am: 'AM',
                pm: 'PM'
            },
        formatter: {
            date: function (date, settings) {
                if (!date) return '';
                var day = date.getDate();
                var month = date.getMonth() + 1;
                var year = date.getFullYear();
                return day + '/' + month + '/' + year;
        }},
        parser: {
            date: function (text, settings) {
                text = text.split('/');
                text=new Date(text[2],text[1]-1,text[0]);
                return text;
            }
        }
    })
}