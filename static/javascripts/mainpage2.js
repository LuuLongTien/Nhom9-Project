// const footerUlIntro = document.createElement('ul');
// footerUlIntro.className = 'footer-intro';

// const footerLiIntro1 = document.createElement('li');
// footerLiIntro1.className = 'footer-intro-name';
// footerLiIntro1.innerText = 'Phạm Xuân Quân';

// const footerLiIntro1a = document.createElement('a');
// footerLiIntro1a.className = 'footer-intro-name-link';
// const footerLiIntro1ai = document.createElement('i');
// footerLiIntro1ai.className = 'header__navbar-icon fab fa-instagram' 

// footerLiIntro1a.appendChild(footerLiIntro1ai);

// const footerLiIntro2 = document.createElement('li');             Test-for-me
// footerLiIntro2.className = 'footer-intro-name';
// footerLiIntro2.innerText = 'Phạm Xuân Quân';

// const footerLiIntro3 = document.createElement('li');
// footerLiIntro3.className = 'footer-intro-name';
// footerLiIntro3.innerText = 'Phạm Xuân Quân';

// const footerLiIntro4 = document.createElement('li');
// footerLiIntro4.className = 'footer-intro-name';
// footerLiIntro4.innerText = 'Phạm Xuân Quân';

// footerUlIntro.appendChild(footerLiIntro1)
// footerUlIntro.appendChild(footerLiIntro1a)
// footerUlIntro.appendChild(footerLiIntro2)
// footerUlIntro.appendChild(footerLiIntro3)
// footerUlIntro.appendChild(footerLiIntro4)

// document.body.appendChild(footerUlIntro);

const footerUlIntro = React.createElement(
    'ul',
    {
        className: 'footer-list'
    },
    React.createElement('h2', {className:'footer-list-name-text'}, 'Về chúng tôi'),


    React.createElement('li', {className: 'footer-list-name'}, 'Phạm Xuân Quân', 
        React.createElement('a', {className: 'footer-list-name-link'}, 
            React.createElement('i', {className: 'header__navbar-icon  fab fa-facebook'}, null))),

    React.createElement('li', {className: 'footer-list-name'}, 'Phạm Xuân Quân', 
        React.createElement('a', {className: 'footer-list-name-link'}, 
            React.createElement('i', {className: 'header__navbar-icon  fab fa-facebook'}, null))),

    React.createElement('li', {className: 'footer-list-name'}, 'Phạm Xuân Quân', 
        React.createElement('a', {className: 'footer-list-name-link'}, 
            React.createElement('i', {className: 'header__navbar-icon  fab fa-facebook'}, null))),

    React.createElement('li', {className: 'footer-list-name'}, 'Phạm Xuân Quân', 
        React.createElement('a', {className: 'footer-list-name-link'}, 
            React.createElement('i', {className: 'header__navbar-icon  fab fa-facebook'}, null))),

    React.createElement('li', {className: 'footer-list-name'}, 'Phạm Xuân Quân', 
        React.createElement('a', {className: 'footer-list-name-link'}, 
            React.createElement('i', {className: 'header__navbar-icon  fab fa-facebook'}, null))),

)

const footer = document.querySelector('.footer');

ReactDOM.render(footerUlIntro, footer);

// 2

const footerUlPath = React.createElement(
    'ul', 
    {
        className: 'footer-path'
    }, 
    React.createElement(
        'h2',
        {className: 'footer-path-text'},
        'Đường dẫn'
        ),
    
    React.createElement('li', {className: 'footer-path-list'}, 
        React.createElement('a', null, 'Trang chủ' )   
    ),
    React.createElement('li', {className: 'footer-path-list'}, 
        React.createElement('a', null, 'Về chúng tôi' )   
    ),
    React.createElement('li', {className: 'footer-path-list'}, 
        React.createElement('a', null, 'Thông tin liên lạc' )   
    ),
    React.createElement('li', {className: 'footer-path-list'}, 
        React.createElement('a', null, 'Dịch vụ' )   
    ),
    React.createElement('li', {className: 'footer-path-list'}, 
        React.createElement('a', null, 'Điều kiện và chính sách' )   
    ),
    );

    // ReactDOM.render(footerUlPath, footer);
    

