const slideNavProfileModalDown = [
    { transform: 'translateY(-100%)' },
    { transform: 'translateY(0)' }
];
const slideNavProfileModalUp = [
    { transform: 'translateY(0)' },
    { transform: 'translateY(-100%)' }
];
const slideSidePanelIntoView = [
    { transform: 'translateX(100%)' },
    { transform: 'translateX(0%)' }
];
const slideSidePanelOutOfView = [
    { transform: 'translateX(0%)' },
    { transform: 'translateX(100%)' }
]
const animationDelay = 550;
const slideTiming = { duration: animationDelay, easing: 'ease-in-out'};

function openUserProfileModal() {
    let userNavProfile = document.querySelector('div#user-nav-profile');
    let userNavProfileModal = document.getElementById('user-nav-profile-modal');
    userNavProfileModal.style.display = 'block';
    userNavProfileModal.animate(slideNavProfileModalDown, slideTiming);
    userNavProfile.firstChild.style.filter = 'brightness(70%)';
}

document.addEventListener('DOMContentLoaded', function () {
    let userNavProfile = document.querySelector('div#user-nav-profile');
    let userNavProfileModal = document.getElementById('user-nav-profile-modal');

    // Reset hamburger menu icon to default state
    document.querySelector('#nav-menu-checkbox').checked = false;

    // Open user profile modal when icon in navbar is clicked 
    userNavProfile.onclick = function () {
        userNavProfileModal.style.display = 'block';
        userNavProfileModal.animate(slideNavProfileModalDown, slideTiming);
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
    let userNavProfileModal = document.getElementById('user-nav-profile-modal');
    let navProfileModalBoundingBox = userNavProfileModal.getBoundingClientRect();
    let x = event.clientX, y = event.clientY;
    
    if (event.target.id === 'user-nav-profile-img' || event.target.parentNode.id === 'user-nav-profile') return;
    if (event.target.id === 'register-signin-btn') return;

    console.info(`Conditions to close: \
    \n${x} < ${navProfileModalBoundingBox.left}: ${x < navProfileModalBoundingBox.left}\
    \n${y} > ${navProfileModalBoundingBox.bottom}: ${y > navProfileModalBoundingBox.bottom}`);
    
    if (x < navProfileModalBoundingBox.left || y > navProfileModalBoundingBox.bottom) {
        userNavProfileModal.animate(slideNavProfileModalUp, slideTiming);
        setTimeout(function () {
            userNavProfileModal.style.display = 'none';
        }, animationDelay);
        userNavProfile.firstChild.style.filter = 'brightness(100%)';
        return;
    }
}

function toggleNavMobileMenu() {
    console.log("Hamburger menu toggled");
    let sidePanelMenu = document.querySelector('#side-panel-menu')

    if (!sidePanelMenu.classList.contains('hidden')) {
        document.querySelector('#overlay').style.display = 'none';
        console.log("Overlay added");
        sidePanelMenu.animate(slideSidePanelOutOfView, slideTiming);
        setTimeout(function() {
            sidePanelMenu.classList.add('hidden');
        }, animationDelay);
        
    } else {
        document.querySelector('#overlay').style.display = 'block';
        console.log("Overlay removed");
        sidePanelMenu.classList.remove('hidden');
        sidePanelMenu.animate(slideSidePanelIntoView, slideTiming);
    }
}

function closeAlertMessages() {
    let alertNav = document.querySelector('#alert-messages-nav');
    alertNav.style.display = 'none';
}

function disableProfileInputsState(state) {
    let ids = ['firstname', 'lastname', 'image', 'username', 'address', 'email', 'dob', 'sex', 'password', 'password-repeat', 'contactno', 'emgcy-fname', 'emgcy-lname', 'relationship', 'emgcy-contactno'];
    let disabled_ids = ['sex'];
    for (let id of ids) {
        let el = document.getElementById(id);
        state == true ? el.setAttribute("readonly", "readonly") : el.removeAttribute("readonly");
    }
    for (let disabled_id of disabled_ids) {
        let disabled_el = document.querySelector(`#disabled-${disabled_id}`);
        state == true ? disabled_el.classList.remove('hidden') : disabled_el.classList.add('hidden');
        disabled_el = document.querySelector(`#${disabled_id}`);
        state == true ? disabled_el.classList.add('hidden') : disabled_el.classList.remove('hidden');
    }

    // Show image inputs
    let imageContainer = document.querySelector('#image');
    state == true ? imageContainer.classList.add('hidden') : imageContainer.classList.remove('hidden');

    // Show password inputs
    let passwordContainer = document.querySelector('#password-container');
    state == true ? passwordContainer.classList.add('hidden') : passwordContainer.classList.remove('hidden');
}

function makeProfileEditable() {
    let editProfileBtn = document.querySelector('#edit-profile-btn');
    let cancelEditProfileBtn = document.querySelector('#cancel-edit-profile-btn');
    let saveProfileBtn = document.querySelector('#save-profile-btn');
    editProfileBtn.style.display = 'none';
    cancelEditProfileBtn.style.display = 'flex';
    cancelEditProfileBtn.style.justifyContent = 'center';
    saveProfileBtn.style.display = 'block';
    disableProfileInputsState(false);
    document.querySelector('#edit-profile-form').scrollIntoView({
        behavior: 'smooth'
    });
    document.querySelector('#image').onchange = function () {
        document.querySelector('#profile-image-preview').src = URL.createObjectURL(this.files[0]);
    }

    saveProfileBtn.onclick = function () {
        disableProfileInputsState(true);
        saveProfileBtn.style.display = 'none';
        cancelEditProfileBtn.style.display = 'none';
        editProfileBtn.style.display = 'flex';
        editProfileBtn.style.justifyContent = 'center';
    }

    cancelEditProfileBtn.onclick = function () {
        disableProfileInputsState(true);
        saveProfileBtn.style.display = 'none';
        cancelEditProfileBtn.style.display = 'none';
        editProfileBtn.style.display = 'flex';
        editProfileBtn.style.justifyContent = 'center';
        document.getElementById('edit-profile-form').reset();
        console.log('Form reset');
    }
}