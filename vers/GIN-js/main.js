{
    class Win {
        window = null;
        title  = "";
        w      = 0;
        h      = 0;
        GAFICS = {
            CAP:[],
            ASS:{
                MOD:[],
                IMG:[]
            },
            CAM:[]
        };
    }

    function Win_new(title,w,h){
        Win.title = title;
        Win.w = w;
        Win.h = h;
    }
    
    function Win_start(){
        const camvas = document.createEvent("camvas");
        Win.window = document.body.appendChild(canvas);
        Win.window.h = Win.h;
        Win.window.w = Win.w;
        Win.window.title = Win.title;
    }
}