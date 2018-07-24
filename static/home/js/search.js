var info = location.search.split('=')[1]
$.get('/blog/search_info/?info='+info,function (data) {
    var li_html = template('info_ul',{articles:data.articles})
    $('.search-wrap-list-ul').html(li_html)
})