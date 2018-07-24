var article_id = location.search.split('=')[1]
$.get('/info/article_info/'+article_id ,function (data) {
    console.log(data)
    $('.t-h1').html(data.article.title)
    $('.column-link').html(data.data.type)
    $('#image').attr('src',data.article.img)
    $('.article-content-wrap').html(data.article.content)
    $('#face').attr('src','/static/'+ data.data.auth_img)
    $('#u_name').html(data.data.auth_name)
    var li_html = template('li_list',{articls_list:data.data.article_list})
    $('#ul_text').html(li_html)
})