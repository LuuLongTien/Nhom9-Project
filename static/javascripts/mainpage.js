const $ = document.querySelector.bind(document)
const $$ = document.querySelectorAll.bind(document);

const tabs = $$('.content-list-name');
const panes = $$('.grid__panes');


 tabs.forEach( (tab, index) => {       //Lặp qua các ptu cua tabs
    const pane = panes[index]

    tab.onclick = function(){
       
        $(".testjs").classList.remove("testjs")
        $('.grid__panes.exit').classList.remove('exit')
        $('.content').classList.remove('panes-fix')

        this.classList.add('testjs')   //add class exitjs vào thẻ
        pane.classList.add('exit')   //add class exitjs vào thẻ
 

    }
});

