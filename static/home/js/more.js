

$(document).ready(function(){

    /*初始化*/
    var counter = 0; /*计数器*/
    var pageStart = 0; /*offset*/
    var pageSize = 5; /*size*/

    /*首次加载*/
    getData(pageStart, pageSize);

    /*监听加载更多*/
    $(document).on('click', '#more_than', function(){
        counter += 1;
        pageStart = counter * pageSize;

        getData(pageStart, pageSize);
    });
});


function getData(offset,size){
    $.ajax({
        type: 'GET',
        url: '/blog/index_article/',
        dataType: 'json',
        success: function(msg){

            var data = msg.articles;
            var sum = msg.articles.length;
            var result = '';

            /****业务逻辑块：实现拼接html内容并append到页面*********/

            //console.log(offset , size, sum);

            /*如果剩下的记录数不够分页，就让分页数取剩下的记录数
            * 例如分页数是5，只剩2条，则只取2条

            * 实际MySQL查询时不写这个不会有问题
            */
            // offset=0,size=5,sum为文章集的总长度
            if(sum - offset < size ){
                size = sum - offset;
            }

            /*使用for循环模拟SQL里的limit(offset,size)*/
            for(var i=offset; i< (offset+size); i += 1){

                result += ' <div class="mod-b mod-art" data-aid='+data[i].id+'>\n' +
                    '            \t <div class="mod-angle">热</div>\n' +
                    '                 <div class="mod-thumb ">\n' +
                    '                       <a class="transition" title=' + data[i].title + ' href="#" target="_blank">\n' +
                    '\t\t\t\t\t\t  <img class="lazy" src=' + data[i].img + ' alt="'+ data[i].title + '">\n' +
                    '                       </a>\n' +
                    '                 </div>\n' +
                    '                 <div class="column-link-box">\n' +
                    '                 \t<a href="#" class="column-link" target="_blank">娱乐淘金</a>\n' +
                    '                 </div>\n' +
                    '                 <div class="mob-ctt">\n' +
                    '                    <h2><a href="#" class="transition msubstr-row2" target="_blank">' + data[i].title + '</a></h2>\n' +
                    '\t\t\t\t\t<div class="mob-author">\n' +
                    '                         <div class="author-face">\n' +
                    '                              <a href="#" target="_blank"><img src='+ data[i].img + '></a>\n' +
                    '                         </div>\n' +
                    '                         <a href="#" target="_blank">\n' +
                    '                            <span class="author-name ">量子位</span>\n' +
                    '                         </a>\n' +
                    '                         <a href="#" target="_blank" title="购买VIP会员"></a>\n' +
                    '                         <span class="time">1小时前</span>\n' +
                    '                         <i class="icon icon-cmt"></i><em>0</em>\n' +
                    '                         <i class="icon icon-fvr"></i><em>0</em>\n' +
                    '                    </div>\n' +
                    '                    <div class="mob-sub">'+ data[i].title +'</div>\n' +
                    '                 </div>\n' +
                    '            </div>'

            }

            $('.mod-info-flow').append(result);

            /*隐藏more按钮*/
            if ( (offset + size) >= sum){
                $(".js-get-mod-more-list").hide();
            }else{
                $(".js-get-mod-more-list").show();
            }
        },
        error: function(xhr, type){
            alert('error!');
        }
    });
}
