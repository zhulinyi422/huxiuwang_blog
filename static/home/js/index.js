$(document).ready(function () {
    $.get('/blog/index/',function (data) {
        if (data.code == 200){
            $('.login-link-box').hide()
            $('.cd-signup').hide()
            $('#username').html(data.username)
        }else {
            $('.login-link-box').show()
            $('.cd-signup').show()
        }
    })
    $.get('/blog/info_list/',function (data) {
        var li_html = template('info_li_list',{types:data.type_lists})
        $('#ul_text').html(li_html)
    })
    $.get('/blog/index_article/',function (data) {
        console.log(data)
        var content_html = template('content_list',{contents:data.articles})
        $('.mod-info-flow').html(content_html)
    });

    $('#search_form').submit(function () {
        data = $('#search-input').val();
        location.href='/blog/search/?info='+data
        return false
    })

})

