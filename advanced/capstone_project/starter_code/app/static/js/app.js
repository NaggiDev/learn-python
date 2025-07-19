// Main JavaScript file for Data Analytics Dashboard

// Global variables
let currentUser = null;
let authToken = null;

// API base URL
const API_BASE_URL = '/api';

// Initialize application
document.addEventListener('DOMContentLoaded', function () {
    initializeApp();
});

function initializeApp() {
    // Check authentication status
    checkAuthStatus();

    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize file upload areas
    initializeFileUpload();
}

// Authentication functions
async function checkAuthStatus() {
    try {
        const response = await fetch('/auth/profile');
        if (response.ok) {
            const data = await response.json();
            currentUser = data.user;
            updateUIForAuthenticatedUser();
        } else {
            currentUser = null;
            updateUIForUnauthenticatedUser();
        }
    } catch (error) {
        console.error('Error checking auth status:', error);
        currentUser = null;
        updateUIForUnauthenticatedUser();
    }
}

function updateUIForAuthenticatedUser() {
    // Update navigation
    const userDropdown = document.getElementById('userDropdown');
    if (userDropdown && currentUser) {
        userDropdown.innerHTML = `<i class="fas fa-user"></i> ${currentUser.username}`;
    }

    // Hide login/register modals if shown
    const loginModal = bootstrap.Modal.getInstance(document.getElementById('loginModal'));
    const registerModal = bootstrap.Modal.getInstance(document.getElementById('registerModal'));
    if (loginModal) loginModal.hide();
    if (registerModal) registerModal.hide();
}

function updateUIForUnauthenticatedUser() {
    // Show login modal if on a protected page
    const protectedPages = ['/dashboard', '/datasets', '/analysis', '/visualizations'];
    if (protectedPages.some(page => window.location.pathname.includes(page))) {
        showLoginModal();
    }
}

function showLoginModal() {
    const loginModal = new bootstrap.Modal(document.getElementById('loginModal'));
    if (loginModal) {
        loginModal.show();
    }
}

function showRegister() {
    const loginModal = bootstrap.Modal.getInstance(document.getElementById('loginModal'));
    const registerModal = new bootstrap.Modal(document.getElementById('registerModal'));

    if (loginModal) loginModal.hide();
    if (registerModal) registerModal.show();
}

function showLogin() {
    const registerModal = bootstrap.Modal.getInstance(document.getElementById('registerModal'));
    const loginModal = new bootstrap.Modal(document.getElementById('loginModal'));

    if (registerModal) registerModal.hide();
    if (loginModal) loginModal.show();
}

async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const remember = document.getElementById('remember').checked;

    if (!username || !password) {
        showAlert('Please enter both username and password', 'danger');
        return;
    }

    try {
        const response = await fetch('/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: username,
                password: password,
                remember: remember
            })
        });

        const data = await response.json();

        if (response.ok) {
            currentUser = data.user;
            updateUIForAuthenticatedUser();
            showAlert('Login successful!', 'success');

            // Reload page to update content
            setTimeout(() => {
                window.location.reload();
            }, 1000);
        } else {
            showAlert(data.error || 'Login failed', 'danger');
        }
    } catch (error) {
        console.error('Login error:', error);
        showAlert('Login failed. Please try again.', 'danger');
    }
}

async function register() {
    const username = document.getElementById('regUsername').value;
    const email = document.getElementById('regEmail').value;
    const password = document.getElementById('regPassword').value;
    const passwordConfirm = document.getElementById('regPasswordConfirm').value;

    if (!username || !email || !password || !passwordConfirm) {
        showAlert('Please fill in all fields', 'danger');
        return;
    }

    if (password !== passwordConfirm) {
        showAlert('Passwords do not match', 'danger');
        return;
    }

    try {
        const response = await fetch('/auth/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: username,
                email: email,
                password: password
            })
        });

        const data = await response.json();

        if (response.ok) {
            showAlert('Registration successful! Please log in.', 'success');
            showLogin();
        } else {
            showAlert(data.error || 'Registration failed', 'danger');
        }
    } catch (error) {
        console.error('Registration error:', error);
        showAlert('Registration failed. Please try again.', 'danger');
    }
}

async function logout() {
    try {
        const response = await fetch('/auth/logout', {
            method: 'POST'
        });

        if (response.ok) {
            currentUser = null;
            showAlert('Logged out successfully', 'info');

            // Redirect to home page
            setTimeout(() => {
                window.location.href = '/';
            }, 1000);
        }
    } catch (error) {
        console.error('Logout error:', error);
        showAlert('Logout failed', 'danger');
    }
}

function showProfile() {
    // TODO: Implement profile modal
    console.log('Show profile modal');
}

// Utility functions
function showAlert(message, type = 'info') {
    const alertContainer = document.getElementById('flash-messages');
    if (!alertContainer) return;

    const alertId = 'alert-' + Date.now();
    const alertHTML = `
        <div id="${alertId}" class="alert alert-${type} alert-dismissible fade show" role="alert">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;

    alertContainer.innerHTML = alertHTML;

    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        const alert = document.getElementById(alertId);
        if (alert) {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }
    }, 5000);
}

function showSpinner(show = true) {
    let spinner = document.getElementById('spinner-overlay');

    if (show) {
        if (!spinner) {
            spinner = document.createElement('div');
            spinner.id = 'spinner-overlay';
            spinner.className = 'spinner-overlay';
            spinner.innerHTML = `
                <div class="spinner-border text-primary" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
            `;
            document.body.appendChild(spinner);
        }
        spinner.style.display = 'flex';
    } else {
        if (spinner) {
            spinner.style.display = 'none';
        }
    }
}

function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';

    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));

    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
}

// File upload functionality
function initializeFileUpload() {
    const uploadAreas = document.querySelectorAll('.file-upload-area');

    uploadAreas.forEach(area => {
        area.addEventListener('dragover', handleDragOver);
        area.addEventListener('dragleave', handleDragLeave);
        area.addEventListener('drop', handleDrop);
        area.addEventListener('click', () => {
            const fileInput = area.querySelector('input[type="file"]');
            if (fileInput) fileInput.click();
        });
    });
}

function handleDragOver(e) {
    e.preventDefault();
    e.currentTarget.classList.add('dragover');
}

function handleDragLeave(e) {
    e.preventDefault();
    e.currentTarget.classList.remove('dragover');
}

function handleDrop(e) {
    e.preventDefault();
    e.currentTarget.classList.remove('dragover');

    const files = e.dataTransfer.files;
    if (files.length > 0) {
        handleFileSelection(files[0], e.currentTarget);
    }
}

function handleFileSelection(file, uploadArea) {
    // Update UI to show selected file
    const fileName = uploadArea.querySelector('.file-name');
    const fileSize = uploadArea.querySelector('.file-size');

    if (fileName) fileName.textContent = file.name;
    if (fileSize) fileSize.textContent = formatFileSize(file.size);

    // Enable upload button
    const uploadBtn = uploadArea.querySelector('.upload-btn');
    if (uploadBtn) {
        uploadBtn.disabled = false;
        uploadBtn.onclick = () => uploadFile(file);
    }
}

async function uploadFile(file) {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('name', file.name);
    formData.append('description', '');

    try {
        showSpinner(true);

        const response = await fetch(`${API_BASE_URL}/datasets`, {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (response.ok) {
            showAlert('File uploaded successfully!', 'success');
            // Refresh datasets list if on datasets page
            if (typeof loadDatasets === 'function') {
                loadDatasets();
            }
        } else {
            showAlert(data.error || 'Upload failed', 'danger');
        }
    } catch (error) {
        console.error('Upload error:', error);
        showAlert('Upload failed. Please try again.', 'danger');
    } finally {
        showSpinner(false);
    }
}

// API helper functions
async function apiRequest(endpoint, options = {}) {
    const url = `${API_BASE_URL}${endpoint}`;
    const defaultOptions = {
        headers: {
            'Content-Type': 'application/json',
        }
    };

    const finalOptions = { ...defaultOptions, ...options };

    try {
        const response = await fetch(url, finalOptions);
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || `HTTP error! status: ${response.status}`);
        }

        return data;
    } catch (error) {
        console.error('API request error:', error);
        throw error;
    }
}

// Export functions for use in other scripts
window.DataAnalyticsDashboard = {
    checkAuthStatus,
    login,
    register,
    logout,
    showAlert,
    showSpinner,
    formatFileSize,
    formatDate,
    apiRequest
};