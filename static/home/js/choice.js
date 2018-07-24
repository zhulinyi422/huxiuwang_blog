$(document).ready(function () {
    id = location.search.split('=')[1]
    $.get('/blog/choice/'+id+'/',function (data) {
        $('#title').html(data.typename+'-虎嗅网')
        $('.type').html(data.typename)
        var div_html = template('div_list',{divs:data.article_list})
        $('#div_content').html(div_html)
        var li_html = template('li_list',{lis:data.pindao_list})
        $('#ul_content').html(li_html)
        $('#hot_text').html(data.typename+'-热文')
    })
    $.get('/blog/choice_hot/'+id+'/',function (data) {
        console.log(data)
        var li_html = template('hot_content',{hots:data.hot_content})
        $('#hot_ul').html(li_html)
    })

    $.get('/blog/info_list/',function (data) {
        var li_html = template('info_li_list',{types:data.type_lists})
        $('#ul_text').html(li_html)
    })
})