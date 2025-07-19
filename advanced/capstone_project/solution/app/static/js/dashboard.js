// Dashboard JavaScript
class DashboardApp {
    constructor() {
        this.currentUser = null;
        this.datasets = [];
        this.currentSection = 'datasets';
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.checkAuthStatus();
    }

    setupEventListeners() {
        // Navigation
        document.querySelectorAll('[data-section]').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                this.showSection(e.target.dataset.section);
            });
        });

        // Authentication
        document.getElementById('loginForm').addEventListener('submit', (e) => {
            e.preventDefault();
            this.login();
        });

        document.getElementById('registerForm').addEventListener('submit', (e) => {
            e.preventDefault();
            this.register();
        });

        document.getElementById('showRegister').addEventListener('click', (e) => {
            e.preventDefault();
            this.showRegisterForm();
        });

        document.getElementById('showLogin').addEventListener('click', (e) => {
            e.preventDefault();
            this.showLoginForm();
        });

        document.getElementById('logoutBtn').addEventListener('click', (e) => {
            e.preventDefault();
            this.logout();
        });

        // Dataset upload
        document.getElementById('uploadBtn').addEventListener('click', () => {
            this.uploadDataset();
        });

        // Analysis
        document.getElementById('analysisForm').addEventListener('submit', (e) => {
            e.preventDefault();
            this.runAnalysis();
        });

        // Chart creation
        document.getElementById('chartForm').addEventListener('submit', (e) => {
            e.preventDefault();
            this.createChart();
        });

        // Dataset selection for analysis/charts
        document.getElementById('analysisDataset').addEventListener('change', (e) => {
            this.loadDatasetColumns(e.target.value, 'analysis');
        });

        document.getElementById('chartDataset').addEventListener('change', (e) => {
            this.loadDatasetColumns(e.target.value, 'chart');
        });
    }

    async checkAuthStatus() {
        try {
            const response = await fetch('/api/auth/profile');
            if (response.ok) {
                const user = await response.json();
                this.currentUser = user;
                this.showMainDashboard();
            } else {
                this.showLoginForm();
            }
        } catch (error) {
            console.error('Auth check failed:', error);
            this.showLoginForm();
        }
    }

    async login() {
        const username = document.getElementById('loginUsername').value;
        const password = document.getElementById('loginPassword').value;

        try {
            const response = await fetch('/api/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password })
            });

            if (response.ok) {
                const user = await response.json();
                this.currentUser = user;
                this.showAlert('Login successful!', 'success');
                this.showMainDashboard();
            } else {
                const error = await response.json();
                this.showAlert(error.error || 'Login failed', 'danger');
            }
        } catch (error) {
            console.error('Login error:', error);
            this.showAlert('Login failed', 'danger');
        }
    }

    async register() {
        const username = document.getElementById('registerUsername').value;
        const email = document.getElementById('registerEmail').value;
        const password = document.getElementById('registerPassword').value;

        try {
            const response = await fetch('/api/auth/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, email, password })
            });

            if (response.ok) {
                this.showAlert('Registration successful! Please login.', 'success');
                this.showLoginForm();
            } else {
                const error = await response.json();
                this.showAlert(error.error || 'Registration failed', 'danger');
            }
        } catch (error) {
            console.error('Registration error:', error);
            this.showAlert('Registration failed', 'danger');
        }
    }

    async logout() {
        try {
            await fetch('/api/auth/logout', { method: 'POST' });
            this.currentUser = null;
            this.showAlert('Logged out successfully', 'success');
            this.showLoginForm();
        } catch (error) {
            console.error('Logout error:', error);
        }
    }

    showLoginForm() {
        document.getElementById('loginSection').style.display = 'block';
        document.getElementById('registerSection').style.display = 'none';
        document.getElementById('mainDashboard').style.display = 'none';
    }

    showRegisterForm() {
        document.getElementById('loginSection').style.display = 'none';
        document.getElementById('registerSection').style.display = 'block';
        document.getElementById('mainDashboard').style.display = 'none';
    }

    showMainDashboard() {
        document.getElementById('loginSection').style.display = 'none';
        document.getElementById('registerSection').style.display = 'none';
        document.getElementById('mainDashboard').style.display = 'block';

        if (this.currentUser) {
            document.getElementById('username').textContent = this.currentUser.username;
        }

        this.showSection(this.currentSection);
    }

    showSection(section) {
        // Hide all sections
        document.querySelectorAll('.dashboard-section').forEach(el => {
            el.style.display = 'none';
        });

        // Show selected section
        document.getElementById(section + 'Section').style.display = 'block';

        // Update navigation
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
        });
        document.querySelector(`[data-section="${section}"]`).classList.add('active');

        this.currentSection = section;

        // Load section data
        switch (section) {
            case 'datasets':
                this.loadDatasets();
                break;
            case 'analysis':
                this.loadDatasetsForAnalysis();
                break;
            case 'visualizations':
                this.loadDatasetsForCharts();
                break;
            case 'dashboards':
                this.loadDashboards();
                break;
        }
    }

    async loadDatasets() {
        try {
            const response = await fetch('/api/datasets');
            if (response.ok) {
                const data = await response.json();
                this.datasets = data.datasets || [];
                this.renderDatasetsTable();
            } else {
                this.showAlert('Failed to load datasets', 'danger');
            }
        } catch (error) {
            console.error('Load datasets error:', error);
            this.showAlert('Failed to load datasets', 'danger');
        }
    }

    renderDatasetsTable() {
        const container = document.getElementById('datasetsTable');

        if (this.datasets.length === 0) {
            container.innerHTML = `
                <div class="text-center text-muted">
                    <i class="fas fa-database fa-3x mb-3"></i>
                    <p>No datasets uploaded yet</p>
                    <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#uploadModal">
                        Upload Your First Dataset
                    </button>
                </div>
            `;
            return;
        }

        const tableHTML = `
            <div class="table-responsive">
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Type</th>
                            <th>Size</th>
                            <th>Rows</th>
                            <th>Columns</th>
                            <th>Uploaded</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${this.datasets.map(dataset => `
                            <tr class="dataset-row" data-id="${dataset.id}">
                                <td>
                                    <strong>${dataset.name}</strong>
                                    ${dataset.description ? `<br><small class="text-muted">${dataset.description}</small>` : ''}
                                </td>
                                <td><span class="badge bg-secondary">${dataset.file_type.toUpperCase()}</span></td>
                                <td class="file-size">${dataset.file_size_formatted}</td>
                                <td>${dataset.row_count || '-'}</td>
                                <td>${dataset.column_count || '-'}</td>
                                <td class="upload-date">${new Date(dataset.upload_date).toLocaleDateString()}</td>
                                <td>
                                    <button class="btn btn-sm btn-outline-primary me-1" onclick="app.previewDataset(${dataset.id})">
                                        <i class="fas fa-eye"></i>
                                    </button>
                                    <button class="btn btn-sm btn-outline-danger" onclick="app.deleteDataset(${dataset.id})">
                                        <i class="fas fa-trash"></i>
                                    </button>
                                </td>
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
            </div>
        `;

        container.innerHTML = tableHTML;
    }

    async uploadDataset() {
        const fileInput = document.getElementById('datasetFile');
        const nameInput = document.getElementById('datasetName');
        const descriptionInput = document.getElementById('datasetDescription');

        if (!fileInput.files[0]) {
            this.showAlert('Please select a file', 'warning');
            return;
        }

        const formData = new FormData();
        formData.append('file', fileInput.files[0]);
        formData.append('name', nameInput.value);
        formData.append('description', descriptionInput.value);

        try {
            const response = await fetch('/api/datasets', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                this.showAlert('Dataset uploaded successfully!', 'success');
                bootstrap.Modal.getInstance(document.getElementById('uploadModal')).hide();
                document.getElementById('uploadForm').reset();
                this.loadDatasets();
            } else {
                const error = await response.json();
                this.showAlert(error.error || 'Upload failed', 'danger');
            }
        } catch (error) {
            console.error('Upload error:', error);
            this.showAlert('Upload failed', 'danger');
        }
    }

    async deleteDataset(id) {
        if (!confirm('Are you sure you want to delete this dataset?')) {
            return;
        }

        try {
            const response = await fetch(`/api/datasets/${id}`, {
                method: 'DELETE'
            });

            if (response.ok) {
                this.showAlert('Dataset deleted successfully', 'success');
                this.loadDatasets();
            } else {
                this.showAlert('Failed to delete dataset', 'danger');
            }
        } catch (error) {
            console.error('Delete error:', error);
            this.showAlert('Failed to delete dataset', 'danger');
        }
    }

    async previewDataset(id) {
        try {
            const response = await fetch(`/api/datasets/${id}/preview`);
            if (response.ok) {
                const data = await response.json();
                this.showDatasetPreview(data);
            } else {
                this.showAlert('Failed to load preview', 'danger');
            }
        } catch (error) {
            console.error('Preview error:', error);
            this.showAlert('Failed to load preview', 'danger');
        }
    }

    showDatasetPreview(data) {
        const modalHTML = `
            <div class="modal fade" id="previewModal" tabindex="-1">
                <div class="modal-dialog modal-xl">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">Dataset Preview</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                        </div>
                        <div class="modal-body">
                            <p><strong>Rows:</strong> ${data.total_rows} | <strong>Columns:</strong> ${data.total_columns}</p>
                            <div class="table-responsive">
                                <table class="table table-sm table-striped">
                                    <thead>
                                        <tr>
                                            ${data.columns.map(col => `<th>${col}</th>`).join('')}
                                        </tr>
                                    </thead>
                                    <tbody>
                                        ${data.data.map(row => `
                                            <tr>
                                                ${data.columns.map(col => `<td>${row[col] || ''}</td>`).join('')}
                                            </tr>
                                        `).join('')}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
        `;

        // Remove existing modal if any
        const existingModal = document.getElementById('previewModal');
        if (existingModal) {
            existingModal.remove();
        }

        document.body.insertAdjacentHTML('beforeend', modalHTML);
        new bootstrap.Modal(document.getElementById('previewModal')).show();
    }

    async loadDatasetsForAnalysis() {
        const select = document.getElementById('analysisDataset');
        select.innerHTML = '<option value="">Select dataset...</option>';

        this.datasets.forEach(dataset => {
            const option = document.createElement('option');
            option.value = dataset.id;
            option.textContent = dataset.name;
            select.appendChild(option);
        });
    }

    async loadDatasetsForCharts() {
        const select = document.getElementById('chartDataset');
        select.innerHTML = '<option value="">Select dataset...</option>';

        this.datasets.forEach(dataset => {
            const option = document.createElement('option');
            option.value = dataset.id;
            option.textContent = dataset.name;
            select.appendChild(option);
        });
    }

    async loadDatasetColumns(datasetId, context) {
        if (!datasetId) return;

        try {
            const response = await fetch(`/api/datasets/${datasetId}/preview?rows=1`);
            if (response.ok) {
                const data = await response.json();

                if (context === 'chart') {
                    this.populateColumnSelects(data.columns);
                }
            }
        } catch (error) {
            console.error('Load columns error:', error);
        }
    }

    populateColumnSelects(columns) {
        const xSelect = document.getElementById('xColumn');
        const ySelect = document.getElementById('yColumn');

        xSelect.innerHTML = '<option value="">Select column...</option>';
        ySelect.innerHTML = '<option value="">Select column...</option>';

        columns.forEach(column => {
            const xOption = document.createElement('option');
            xOption.value = column;
            xOption.textContent = column;
            xSelect.appendChild(xOption);

            const yOption = document.createElement('option');
            yOption.value = column;
            yOption.textContent = column;
            ySelect.appendChild(yOption);
        });
    }

    async runAnalysis() {
        const datasetId = document.getElementById('analysisDataset').value;
        const analysisType = document.getElementById('analysisType').value;

        if (!datasetId || !analysisType) {
            this.showAlert('Please select dataset and analysis type', 'warning');
            return;
        }

        const resultsContainer = document.getElementById('analysisResults');
        resultsContainer.innerHTML = '<div class="text-center"><div class="spinner-border" role="status"></div></div>';

        try {
            const response = await fetch('/api/analysis/run', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    dataset_id: parseInt(datasetId),
                    analysis_type: analysisType,
                    async: false
                })
            });

            if (response.ok) {
                const data = await response.json();
                this.displayAnalysisResults(data.result);
            } else {
                const error = await response.json();
                resultsContainer.innerHTML = `<div class="alert alert-danger">${error.error}</div>`;
            }
        } catch (error) {
            console.error('Analysis error:', error);
            resultsContainer.innerHTML = '<div class="alert alert-danger">Analysis failed</div>';
        }
    }

    displayAnalysisResults(results) {
        const container = document.getElementById('analysisResults');

        if (results.columns) {
            // Descriptive statistics
            const columnsHTML = Object.entries(results.columns).map(([colName, stats]) => `
                <div class="analysis-result">
                    <h6>${colName}</h6>
                    <div class="row">
                        <div class="col-md-3">
                            <div class="stat-value">${stats.count}</div>
                            <div class="stat-label">Count</div>
                        </div>
                        ${stats.mean !== undefined ? `
                            <div class="col-md-3">
                                <div class="stat-value">${stats.mean.toFixed(2)}</div>
                                <div class="stat-label">Mean</div>
                            </div>
                            <div class="col-md-3">
                                <div class="stat-value">${stats.std.toFixed(2)}</div>
                                <div class="stat-label">Std Dev</div>
                            </div>
                        ` : ''}
                        <div class="col-md-3">
                            <div class="stat-value">${stats.unique_count}</div>
                            <div class="stat-label">Unique</div>
                        </div>
                    </div>
                </div>
            `).join('');

            container.innerHTML = columnsHTML;
        } else if (results.correlation_matrix) {
            // Correlation analysis
            container.innerHTML = `
                <div class="analysis-result">
                    <h6>Correlation Matrix</h6>
                    <p>Method: ${results.method}</p>
                    <div class="table-responsive">
                        <table class="table table-sm">
                            <thead>
                                <tr>
                                    <th></th>
                                    ${Object.keys(results.correlation_matrix).map(col => `<th>${col}</th>`).join('')}
                                </tr>
                            </thead>
                            <tbody>
                                ${Object.entries(results.correlation_matrix).map(([rowCol, values]) => `
                                    <tr>
                                        <th>${rowCol}</th>
                                        ${Object.values(values).map(val => `<td>${val ? val.toFixed(3) : '-'}</td>`).join('')}
                                    </tr>
                                `).join('')}
                            </tbody>
                        </table>
                    </div>
                </div>
            `;
        } else {
            container.innerHTML = '<div class="alert alert-info">Analysis completed</div>';
        }
    }

    async createChart() {
        const datasetId = document.getElementById('chartDataset').value;
        const chartType = document.getElementById('chartType').value;
        const xColumn = document.getElementById('xColumn').value;
        const yColumn = document.getElementById('yColumn').value;

        if (!datasetId || !chartType) {
            this.showAlert('Please select dataset and chart type', 'warning');
            return;
        }

        const previewContainer = document.getElementById('chartPreview');
        previewContainer.innerHTML = '<div class="text-center"><div class="spinner-border" role="status"></div></div>';

        try {
            const response = await fetch('/api/visualizations/chart', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    dataset_id: parseInt(datasetId),
                    chart_type: chartType,
                    x_column: xColumn || undefined,
                    y_column: yColumn || undefined,
                    format: 'html'
                })
            });

            if (response.ok) {
                const data = await response.json();
                previewContainer.innerHTML = data.chart_data;
            } else {
                const error = await response.json();
                previewContainer.innerHTML = `<div class="alert alert-danger">${error.error}</div>`;
            }
        } catch (error) {
            console.error('Chart creation error:', error);
            previewContainer.innerHTML = '<div class="alert alert-danger">Chart creation failed</div>';
        }
    }

    async loadDashboards() {
        const container = document.getElementById('dashboardsList');
        container.innerHTML = '<div class="text-center text-muted"><p>Dashboard management coming soon...</p></div>';
    }

    showAlert(message, type = 'info') {
        const alertHTML = `
            <div class="alert alert-${type} alert-dismissible fade show" role="alert">
                ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            </div>
        `;

        const container = document.getElementById('alertContainer');
        container.insertAdjacentHTML('beforeend', alertHTML);

        // Auto-dismiss after 5 seconds
        setTimeout(() => {
            const alert = container.querySelector('.alert');
            if (alert) {
                bootstrap.Alert.getOrCreateInstance(alert).close();
            }
        }, 5000);
    }
}

// Initialize the app
const app = new DashboardApp();