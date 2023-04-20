const slideModalDown = [
    { transform: 'translateY(-100%)' },
    { transform: 'translateY(0)' }
];

const slideModalUp = [
    { transform: 'translateY(0)' },
    { transform: 'translateY(-100%)' }
];

const animationDelay = 550;
const slideTiming = { duration: animationDelay, easing: 'ease-in-out'};

function openUserProfileModal() {
    let userNavProfile = document.querySelector('div#user-nav-profile');
    let userNavProfileModal = document.getElementById('user-nav-profile-modal');
    userNavProfileModal.style.display = 'block';
    userNavProfileModal.animate(slideModalDown, slideTiming);
    userNavProfile.firstChild.style.filter = 'brightness(70%)';
}

document.addEventListener('DOMContentLoaded', function () {
    let userNavProfile = document.querySelector('div#user-nav-profile');
    let userNavProfileModal = document.getElementById('user-nav-profile-modal');

    // Open user profile modal when icon in navbar is clicked 
    userNavProfile.onclick = function () {
        userNavProfileModal.style.display = 'block';
        userNavProfileModal.animate(slideModalDown, slideTiming);
        userNavProfile.firstChild.style.filter = 'brightness(70%)';
        return;
    }

    // Move view to top of page when #scroll-to-top-arrow is clicked
    document.querySelector('#scroll-to-top-arrow').onclick = function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
});

// If the user clicks anywhere outside of the modal (denoted by bounding box), close it
window.onclick = function (event) {
    let userNavProfile = document.querySelector('div#user-nav-profile');
    if (event.target.id === 'user-nav-profile-img') return;
    if (event.target.id === 'register-sign-in-btn') return;
    let userNavProfileModal = document.getElementById('user-nav-profile-modal');
    let navProfileModalBoundingBox = userNavProfileModal.getBoundingClientRect();

    let x = event.clientX, y = event.clientY;
    console.info(`Conditions to close: \
    \n${x} < ${navProfileModalBoundingBox.left}: ${x < navProfileModalBoundingBox.left}\
    \n${y} > ${navProfileModalBoundingBox.bottom}: ${y > navProfileModalBoundingBox.bottom}`);
    
    if (x < navProfileModalBoundingBox.left || y > navProfileModalBoundingBox.bottom) {
        userNavProfileModal.animate(slideModalUp, slideTiming);
        setTimeout(function () {
            userNavProfileModal.style.display = 'none';
        }, animationDelay);
        userNavProfile.firstChild.style.filter = 'brightness(100%)';
        return;
    }
}