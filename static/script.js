document.addEventListener('DOMContentLoaded', function() {
    
    const loginForm = document.querySelector('#login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', async function(event) {
            event.preventDefault();
            
            const formData = new FormData(loginForm);
            const response = await fetch('/login', {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                window.location.href = '/';
            } else {
                alert('Invalid credentials. Please try again.');
            }
        });
    }

    const registerForm = document.querySelector('#register-form');
    if (registerForm) {
        registerForm.addEventListener('submit', async function(event) {
            event.preventDefault();
            
            const formData = new FormData(registerForm);
            const response = await fetch('/register', {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                alert('Registration successful. You can now log in.');
                window.location.href = '/login';
            } else {
                alert('Registration failed. Please try again.');
            }
        });
    }

    const forgotPasswordForm = document.querySelector('#forgot-password-form');
    if (forgotPasswordForm) {
        forgotPasswordForm.addEventListener('submit', async function(event) {
            event.preventDefault();
            
            const formData = new FormData(forgotPasswordForm);
            const response = await fetch('/forgot_password', {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                alert('Password recovery instructions sent to your email.');
                window.location.href = '/login';
            } else {
                alert('Password recovery failed. Please try again.');
            }
        });
    }
});
