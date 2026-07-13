// API Configuration
const API_BASE = 'http://localhost:8000';

// Tab Management
function switchTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Remove active class from all buttons
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected tab
    document.getElementById(tabName).classList.add('active');
    
    // Add active class to clicked button
    event.target.classList.add('active');
}

// File Upload Handling
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');

uploadArea.addEventListener('click', () => fileInput.click());

uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.classList.add('drag-over');
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('drag-over');
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.classList.remove('drag-over');
    
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        handleFileUpload(files[0]);
    }
});

fileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
        handleFileUpload(e.target.files[0]);
    }
});

async function handleFileUpload(file) {
    const statusDiv = document.getElementById('uploadStatus');
    const previewDiv = document.getElementById('previewData');
    
    // Validate file type
    if (!file.name.endsWith('.csv') && !file.name.endsWith('.pdf')) {
        showStatus('Only CSV and PDF files are supported', 'error', statusDiv);
        return;
    }
    
    // Show loading status
    showStatus('Uploading and processing file...', 'loading', statusDiv);
    
    try {
        const formData = new FormData();
        formData.append('file', file);
        
        const response = await fetch(`${API_BASE}/upload`, {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (response.ok) {
            showStatus(`✅ ${data.message}`, 'success', statusDiv);
            
            // Show preview
            if (data.transactions && data.transactions.length > 0) {
                displayTransactionPreview(data.transactions, previewDiv);
            }
            
            // Refresh transactions list
            await refreshTransactions();
        } else {
            showStatus(`❌ Error: ${data.detail}`, 'error', statusDiv);
        }
    } catch (error) {
        showStatus(`❌ Error: ${error.message}`, 'error', statusDiv);
    }
}

function displayTransactionPreview(transactions, previewDiv) {
    let html = '<h4>📊 Preview of Imported Transactions</h4>';
    
    transactions.slice(0, 5).forEach(txn => {
        html += `<div class="preview-item">
            <strong>${txn.date}</strong> - ${txn.description} 
            <span style="float: right; color: var(--danger);">₹${txn.amount}</span>
        </div>`;
    });
    
    if (transactions.length > 5) {
        html += `<div class="preview-item"><em>... and ${transactions.length - 5} more transactions</em></div>`;
    }
    
    previewDiv.innerHTML = html;
    previewDiv.style.display = 'block';
}

function showStatus(message, type, element) {
    element.textContent = message;
    element.className = `status ${type}`;
    element.style.display = 'block';
}

// Transactions Management
async function refreshTransactions() {
    try {
        const response = await fetch(`${API_BASE}/transactions`);
        const data = await response.json();
        
        if (data.status === 'success') {
            displayTransactions(data.transactions);
        }
    } catch (error) {
        console.error('Error fetching transactions:', error);
    }
}

function displayTransactions(transactions) {
    const container = document.getElementById('transactionsList');
    
    if (transactions.length === 0) {
        container.innerHTML = '<p style="text-align: center; color: var(--gray-600);">No transactions yet. Upload a file to get started.</p>';
        return;
    }
    
    let html = '';
    transactions.forEach(txn => {
        const categoryColor = getCategoryColor(txn.category);
        html += `
            <div class="transaction-item">
                <div class="transaction-info">
                    <div class="transaction-date">${txn.date}</div>
                    <div class="transaction-description">${txn.description}</div>
                    <span class="transaction-category" style="background: ${categoryColor}20; color: ${categoryColor};">
                        ${txn.category || 'Uncategorized'}
                    </span>
                </div>
                <div class="transaction-amount">₹${txn.amount.toFixed(2)}</div>
            </div>
        `;
    });
    
    container.innerHTML = html;
    
    // Add filter functionality
    setupTransactionFilters(transactions);
}

function setupTransactionFilters(transactions) {
    const searchInput = document.getElementById('filterSearch');
    const categorySelect = document.getElementById('filterCategory');
    
    function filterTransactions() {
        const searchTerm = searchInput.value.toLowerCase();
        const selectedCategory = categorySelect.value;
        
        const filtered = transactions.filter(txn => {
            const matchesSearch = txn.description.toLowerCase().includes(searchTerm);
            const matchesCategory = !selectedCategory || txn.category === selectedCategory;
            return matchesSearch && matchesCategory;
        });
        
        displayTransactions(filtered);
    }
    
    searchInput.addEventListener('input', filterTransactions);
    categorySelect.addEventListener('change', filterTransactions);
}

function getCategoryColor(category) {
    const colors = {
        'food': '#ef4444',
        'transport': '#f59e0b',
        'entertainment': '#8b5cf6',
        'utilities': '#3b82f6',
        'health': '#10b981',
        'shopping': '#ec4899',
        'transfer': '#6b7280'
    };
    return colors[category] || '#6366f1';
}

// Analysis Functions
async function generateInsights() {
    const button = event.target;
    button.disabled = true;
    button.innerHTML = '<span class="spinner"></span> Analyzing...';
    
    try {
        const response = await fetch(`${API_BASE}/analyze`, {
            method: 'POST'
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            displayAnalysisResult(data.insights);
        } else {
            alert(data.message);
        }
    } catch (error) {
        alert(`Error: ${error.message}`);
    } finally {
        button.disabled = false;
        button.innerHTML = 'Generate Insights';
    }
}

async function detectAnomalies() {
    const button = event.target;
    button.disabled = true;
    button.innerHTML = '<span class="spinner"></span> Analyzing...';
    
    try {
        const response = await fetch(`${API_BASE}/analyze/anomalies`, {
            method: 'POST'
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            displayAnalysisResult(data.anomalies);
        } else {
            alert(data.message);
        }
    } catch (error) {
        alert(`Error: ${error.message}`);
    } finally {
        button.disabled = false;
        button.innerHTML = 'Detect Anomalies';
    }
}

async function categorizeTransactions() {
    const button = event.target;
    button.disabled = true;
    button.innerHTML = '<span class="spinner"></span> Analyzing...';
    
    try {
        const response = await fetch(`${API_BASE}/analyze/categorize`, {
            method: 'POST'
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            displayAnalysisResult(data.message || `Categorized ${data.categorized_count} transactions`);
            await refreshTransactions();
        } else {
            alert(data.message);
        }
    } catch (error) {
        alert(`Error: ${error.message}`);
    } finally {
        button.disabled = false;
        button.innerHTML = 'Auto-Categorize';
    }
}

async function performCustomAnalysis() {
    const prompt = document.getElementById('customPrompt').value;
    
    if (!prompt.trim()) {
        alert('Please enter an analysis question');
        return;
    }
    
    const button = event.target;
    button.disabled = true;
    button.innerHTML = '<span class="spinner"></span> Analyzing...';
    
    try {
        const response = await fetch(`${API_BASE}/analyze/custom`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt })
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            displayAnalysisResult(data.analysis);
        } else {
            alert(data.message);
        }
    } catch (error) {
        alert(`Error: ${error.message}`);
    } finally {
        button.disabled = false;
        button.innerHTML = 'Run Custom Analysis';
    }
}

function displayAnalysisResult(result) {
    const resultDiv = document.getElementById('analysisResult');
    const contentDiv = document.getElementById('analysisContent');
    
    contentDiv.textContent = result;
    resultDiv.style.display = 'block';
    
    // Scroll to result
    resultDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Settings Functions
async function saveSystemPrompt(name = 'default') {
    const textarea = document.getElementById(`${name}Prompt`);
    const content = textarea.value;
    
    if (!content.trim()) {
        alert('Prompt content cannot be empty');
        return;
    }
    
    const button = event.target;
    button.disabled = true;
    button.innerHTML = '<span class="spinner"></span> Saving...';
    
    try {
        const response = await fetch(`${API_BASE}/system-prompt?name=${name}&content=${encodeURIComponent(content)}`, {
            method: 'POST'
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            alert('✅ System prompt saved successfully');
        } else {
            alert(`❌ Error: ${data.detail}`);
        }
    } catch (error) {
        alert(`Error: ${error.message}`);
    } finally {
        button.disabled = false;
        button.innerHTML = 'Save Default Prompt';
    }
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    // Check health status
    fetch(`${API_BASE}/health`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('status').textContent = data.status === 'healthy' ? '✅ Running' : '❌ Error';
        })
        .catch(error => {
            document.getElementById('status').textContent = '❌ Backend not running';
        });

    // Load model name from backend config
    fetch(`${API_BASE}/config`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('modelName').textContent = data.model_name || 'Unknown';
        })
        .catch(error => {
            document.getElementById('modelName').textContent = 'Unknown';
        });
    
    // Load initial transactions
    refreshTransactions();
});
