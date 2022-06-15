const mario = document.querySelector('.mario');
const  jump = () =>{
    if ((event.key == 'ArrowUp')) {
    mario.classList.add('jump');
    setTimeout(() => {
        mario.classList.remove('jump');
    }, 500);
    }
}
document.addEventListener ('keydown', jump)






