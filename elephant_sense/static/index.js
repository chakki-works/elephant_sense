$(function(){
    $("#search").click(function(e) {
        search();
    });
    $("#searchForm").on("keypress", function(e) {
        if (e.keyCode == 13) {
            search();
        }
    });
})

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function search() {
    var message = {
        "query": $("#query").val(),
        "_xsrf": getCookie("_xsrf")
    }
    message["debug"] = true;
    $.post("/e/search", message, function(response) {
        console.log(response);
    });
}
