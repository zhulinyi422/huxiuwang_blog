

$(document).ready(function () {
    $.get('/user/member_g/',function (data) {
        $('#username').html(data.user_info.name)
        $('#company').html('公司:'+data.user_info.company)
        $('#job').html('职业:'+data.user_info.job)
        $('#e_mail').html('邮箱:'+data.user_info.e_mail)
        $('#weibo').html('微博:'+data.user_info.e_mail)
        $('#weixin').html('微信:'+data.user_info.we_chat)
        $('#avatar').attr('src','\\static\\'+data.user_info.avatar)
    })
})

function text() {
    $.get('/user/u_article/',function (data) {
        var article_html = template('article-div',{articles:data.articles})
        $('#article').html(article_html)
    })
}