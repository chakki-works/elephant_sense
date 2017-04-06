Vue.prototype.$http = axios
var app = new Vue({
    el: "#main",
    delimiters: ["[[", "]]"],
    data: {
        debug: true,
        query: "",
        results: []
    },
    methods:{
        search: function(){
            var message = {
                "query": this.query
            }
            message["debug"] = this.debug;
            var self = this;
            self.$http({
                method: "POST",
                url:"/e/search",
                data: message,
                xsrfCookieName: "_xsrf",
                xsrfHeaderName: "X-XSRFToken"
            }).then(function(response) {
                self.results = response.data.posts;
            }).catch(function(error){
                console.log(error);
            });
        }
    }
})
Vue.component("post", {
    props: ["post"],
    delimiters: ["[[", "]]"],
    template: document.querySelector('#postTemplate').innerHTML
})