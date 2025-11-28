<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Panel - AutoRebound</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="assets/dashboard-dragdrop.css">
    <link rel="stylesheet" href="assets/dashboard-animations.css">
    <!-- Collapsible CSS Disabled -->
    <!-- <link rel="stylesheet" href="assets/dashboard-collapsible.css"> -->
    <script>
        // Configure Tailwind for dark mode
        tailwind.config = {
            darkMode: 'class'
        }
    </script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        // Dark mode initialization
        if (localStorage.getItem('darkMode') === 'true' ||
            (!localStorage.getItem('darkMode') && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.classList.add('dark');
        }
    </script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/css/smooth-styles.css">
    <script src="/assets/js/smooth-transitions.js" defer></script>
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .sidebar-item.active {
            background: linear-gradient(90deg, #f97316 0%, #fb923c 100%);
            color: white;
        }
        .tab-content {
            display: none;
        }
        .tab-content.active {
            display: block;
        }
        .settings-tab {
            display: none;
        }
        .settings-tab.active {
            display: block;
        }
        /* Dark mode transitions */
        * {
            transition: background-color 0.3s ease, border-color 0.3s ease;
        }
        /* Dark mode for chart containers */
        .dark .chart-container {
            background: #1f2937;
        }
        /* Toggle switch styles */
        .toggle-switch {
            width: 48px;
            height: 24px;
            background: #d1d5db;
            border-radius: 12px;
            position: relative;
            cursor: pointer;
            transition: background 0.3s;
        }
        .toggle-switch.active {
            background: #f97316;
        }
        .toggle-switch .toggle-ball {
            width: 20px;
            height: 20px;
            background: white;
            border-radius: 50%;
            position: absolute;
            top: 2px;
            left: 2px;
            transition: transform 0.3s;
        }
        .toggle-switch.active .toggle-ball {
            transform: translateX(24px);
        }
    </style>
</head>
<body class="bg-gray-100 dark:bg-gray-900">
    <div class="flex h-screen">
        <!-- Sidebar -->
        <div class="w-64 bg-gray-900 dark:bg-black text-white flex flex-col">
            <div class="p-4">
                <h1 class="text-2xl font-bold">AutoRebound</h1>
                <p class="text-sm text-gray-400 mt-1">Admin Panel</p>
            </div>
            
            <nav class="flex-1 mt-8">
                <a href="?tab=dashboard" class="sidebar-item  flex items-center px-4 py-3 hover:bg-gray-800 transition">
                    <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path>
                    </svg>
                    Dashboard
                </a>
                
                <a href="?tab=inventory" class="sidebar-item  flex items-center px-4 py-3 hover:bg-gray-800 transition">
                    <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path>
                    </svg>
                    Inventory
                </a>
                
                <a href="?tab=orders" class="sidebar-item  flex items-center px-4 py-3 hover:bg-gray-800 transition">
                    <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path>
                    </svg>
                    Orders & Tracking
                                    </a>
                
                <a href="?tab=users" class="sidebar-item  flex items-center px-4 py-3 hover:bg-gray-800 transition">
                    <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path>
                    </svg>
                    Users
                                    </a>

                <a href="?tab=messages" class="sidebar-item  flex items-center px-4 py-3 hover:bg-gray-800 transition">
                    <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                    </svg>
                    Messages
                                    </a>
                <a href="?tab=visitor-details" class="sidebar-item active flex items-center px-4 py-3 hover:bg-gray-800 transition">
                    <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
                    </svg>
                    Visitor Details
                </a>
                
                <a href="?tab=settings" class="sidebar-item  flex items-center px-4 py-3 hover:bg-gray-800 transition">
                    <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path>
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                    </svg>
                    Settings
                </a>
            </nav>
            
            <div class="p-4 border-t border-gray-800">
                <div class="flex items-center justify-between mb-3">
                    <div>
                        <p class="text-sm font-semibold">Admin AutoRebound</p>
                        <p class="text-xs text-gray-400">Administrator</p>
                    </div>
                </div>
                <div class="flex space-x-2">
                    <a href="../index.php" class="flex-1 text-center py-2 bg-gray-800 rounded hover:bg-gray-700 text-sm">
                        View Site
                    </a>
                    <a href="../auth.php?action=logout" class="flex-1 text-center py-2 bg-red-600 rounded hover:bg-red-700 text-sm">
                        Logout
                    </a>
                </div>
            </div>
        </div>
        
        <!-- Main Content -->
        <div class="flex-1 overflow-y-auto">
            <!-- Top Bar -->
            <div class="bg-white dark:bg-gray-800 shadow-sm px-6 py-4">
                <div class="flex items-center justify-between">
                    <h2 class="text-2xl font-semibold text-gray-800 dark:text-white">
                        Visitor-details                    </h2>
                    <div class="flex items-center space-x-4">
                        <span class="text-sm text-gray-500 dark:text-gray-400">
                            Friday, November 28, 2025                        </span>

                        <!-- Dark Mode Toggle -->
                        <div class="flex items-center space-x-2">
                            <svg class="w-5 h-5 text-gray-500 dark:text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>
                            </svg>
                            <div id="darkModeToggle" class="toggle-switch" onclick="toggleDarkMode()">
                                <div class="toggle-ball"></div>
                            </div>
                            <svg class="w-5 h-5 text-gray-500 dark:text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path>
                            </svg>
                        </div>

                        <button onclick="location.reload()" class="text-gray-400 hover:text-gray-600 dark:text-gray-500 dark:hover:text-gray-300">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
                            </svg>
                        </button>
                    </div>
                </div>
            </div>
            
            <!-- Page Content -->
            <div class="p-6">
                                    
<div class="p-6">
    <div class="mb-6">
        <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-4">Enhanced Visitor Details</h2>

        <!-- Filters and Actions -->
        <div class="bg-white dark:bg-gray-800 rounded-lg p-4 border border-gray-200 dark:border-gray-700 mb-4">
            <div class="flex flex-wrap items-center gap-4">
                <!-- Date Filter -->
                <div class="flex items-center gap-2">
                    <label class="text-sm font-medium text-gray-700 dark:text-gray-300">Date:</label>
                    <input type="date"
                           id="visitorDateFilter"
                           value="2025-11-28"
                           class="px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white">
                </div>

                <!-- View Type Filter -->
                <div class="flex items-center gap-2">
                    <label class="text-sm font-medium text-gray-700 dark:text-gray-300">Show:</label>
                    <select id="viewTypeFilter" class="px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white">
                        <option value="all" selected>All Visits</option>
                        <option value="site" >Site Visits Only</option>
                        <option value="products" >Product Views Only</option>
                    </select>
                </div>

                <button onclick="applyFilters()"
                        class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600">
                    Apply Filters
                </button>

                <!-- Reset Buttons -->
                <div class="ml-auto flex gap-2">
                    <button onclick="resetVisitorData('today')"
                            class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
                            title="Reset today's data only">
                        📅 Reset Today
                    </button>
                    <button onclick="resetVisitorData('test')"
                            class="px-4 py-2 bg-yellow-500 text-white rounded-lg hover:bg-yellow-600"
                            title="Remove test data (localhost, generated IPs)">
                        🧹 Clear Test Data
                    </button>
                    <button onclick="resetVisitorData('old')"
                            class="px-4 py-2 bg-orange-500 text-white rounded-lg hover:bg-orange-600"
                            title="Remove data older than 30 days">
                        📆 Clear Old Data
                    </button>
                    <button onclick="resetVisitorData('all')"
                            class="px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600"
                            title="Remove all visitor data">
                        🗑️ Reset All Data
                    </button>
                </div>
            </div>
        </div>

        <!-- Stats Cards -->
        <div class="grid grid-cols-2 md:grid-cols-5 gap-4 mb-6">
            <div class="bg-white dark:bg-gray-800 p-4 rounded-lg border border-gray-200 dark:border-gray-700">
                <div class="text-2xl font-bold text-gray-900 dark:text-white">0</div>
                <div class="text-sm text-gray-600 dark:text-gray-400">Unique Visitors</div>
            </div>
            <div class="bg-white dark:bg-gray-800 p-4 rounded-lg border border-gray-200 dark:border-gray-700">
                <div class="text-2xl font-bold text-gray-900 dark:text-white">0</div>
                <div class="text-sm text-gray-600 dark:text-gray-400">Total Page Views</div>
            </div>
            <div class="bg-white dark:bg-gray-800 p-4 rounded-lg border border-gray-200 dark:border-gray-700">
                <div class="text-2xl font-bold text-gray-900 dark:text-white">0</div>
                <div class="text-sm text-gray-600 dark:text-gray-400">Unique IPs</div>
            </div>
            <div class="bg-white dark:bg-gray-800 p-4 rounded-lg border border-gray-200 dark:border-gray-700">
                <div class="text-2xl font-bold text-gray-900 dark:text-white">0</div>
                <div class="text-sm text-gray-600 dark:text-gray-400">Countries</div>
            </div>
            <div class="bg-white dark:bg-gray-800 p-4 rounded-lg border border-gray-200 dark:border-gray-700">
                <div class="text-2xl font-bold text-gray-900 dark:text-white">0</div>
                <div class="text-sm text-gray-600 dark:text-gray-400">Products Viewed</div>
            </div>
        </div>

        <!-- Top Products Today -->
            </div>

    <!-- Visitors Table -->
    <div class="bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700">
        <table class="w-full">
            <thead class="bg-gray-50 dark:bg-gray-900">
                <tr>
                    <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">Time</th>
                    <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">Visitor</th>
                    <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">Page/Product</th>
                    <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">Location</th>
                    <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">Device</th>
                    <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">IP Address</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-gray-200 dark:divide-gray-700">
                                <tr>
                    <td colspan="6" class="px-4 py-8 text-center text-gray-500 dark:text-gray-400">
                        No visitors found for 2025-11-28                    </td>
                </tr>
                            </tbody>
        </table>
    </div>
</div>

<script>
function applyFilters() {
    const date = document.getElementById('visitorDateFilter').value;
    const view = document.getElementById('viewTypeFilter').value;
    window.location.href = '?tab=visitor-details&date=' + date + '&view=' + view;
}

function resetVisitorData(type) {
    let confirmMsg = '';
    switch(type) {
        case 'all':
            confirmMsg = 'Are you sure you want to DELETE ALL visitor data? This cannot be undone!';
            break;
        case 'today':
            confirmMsg = "Reset today's visitor data? This will clear all visits from today.";
            break;
        case 'old':
            confirmMsg = 'Delete all visitor data older than 30 days?';
            break;
        case 'test':
            confirmMsg = 'Delete all test/localhost visitor data?';
            break;
    }

    if (!confirm(confirmMsg)) {
        return;
    }

    fetch('/api/admin/reset-visitor-data.php', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ type: type })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.message);
            location.reload();
        } else {
            alert('Error: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error resetting visitor data');
    });
}
</script>                            </div>
        </div>
    </div>
    
    <script>
        // Charts data
        const salesData = [];
        const categoryData = [{"category":"cars-trucks","count":"11"},{"category":"classic-cars","count":"1"},{"category":"heavy-equipment","count":"1"},{"category":"rvs-motorhomes","count":"7"}];

        // Dark Mode Toggle Function
        function toggleDarkMode() {
            const html = document.documentElement;
            const toggle = document.getElementById('darkModeToggle');

            if (html.classList.contains('dark')) {
                html.classList.remove('dark');
                toggle.classList.remove('active');
                localStorage.setItem('darkMode', 'false');
            } else {
                html.classList.add('dark');
                toggle.classList.add('active');
                localStorage.setItem('darkMode', 'true');
            }

            // Update Chart.js defaults if available
            if (typeof updateChartDefaults !== 'undefined') {
                updateChartDefaults();
            }

            // Refresh charts with new colors if on dashboard
            setTimeout(() => {
                if (typeof window.categoryChart !== 'undefined' && window.categoryChart) {
                    const isDarkMode = document.documentElement.classList.contains('dark');
                    const chartColors = {
                        textColor: isDarkMode ? '#FFFFFF' : '#374151',
                        borderColor: isDarkMode ? '#374151' : '#ffffff'
                    };

                    // Update chart defaults
                    if (typeof Chart !== 'undefined') {
                        Chart.defaults.color = chartColors.textColor;
                        Chart.defaults.plugins.legend.labels.color = chartColors.textColor;
                    }

                    window.categoryChart.options.plugins.legend.labels.color = chartColors.textColor;
                    window.categoryChart.data.datasets[0].borderColor = chartColors.borderColor;
                    window.categoryChart.update();
                }

                if (typeof window.statusChart !== 'undefined' && window.statusChart) {
                    const isDarkMode = document.documentElement.classList.contains('dark');
                    const chartColors = {
                        textColor: isDarkMode ? '#FFFFFF' : '#374151',
                        borderColor: isDarkMode ? '#374151' : '#ffffff'
                    };

                    window.statusChart.options.plugins.legend.labels.color = chartColors.textColor;
                    window.statusChart.data.datasets[0].borderColor = chartColors.borderColor;
                    window.statusChart.update();
                }
            }, 100);
        }

        // Set initial toggle state
        document.addEventListener('DOMContentLoaded', function() {
            const isDark = document.documentElement.classList.contains('dark');
            const toggle = document.getElementById('darkModeToggle');
            if (isDark && toggle) {
                toggle.classList.add('active');
            }
        });

        // Update chart colors for dark mode
        function updateChartsForDarkMode() {
            const isDark = document.documentElement.classList.contains('dark');
            const textColor = isDark ? '#9CA3AF' : '#374151';
            const gridColor = isDark ? '#374151' : '#E5E7EB';

            // Update chart default colors
            Chart.defaults.color = textColor;
            Chart.defaults.borderColor = gridColor;
        }

        // Mark all as read function
        function markAllAsRead(type) {
            fetch('../api/admin/mark-as-read.php', {
                method: 'POST',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: 'type=' + type + '&mark_all=true'
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    location.reload();
                } else {
                    alert('Error: ' + (data.message || 'Failed to mark as read'));
                }
            })
            .catch(error => {
                alert('Error marking as read');
                console.error(error);
            });
        }

        // Mark individual item as read
        function markAsRead(type, id) {
            fetch('../api/admin/mark-as-read.php', {
                method: 'POST',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: 'type=' + type + '&id=' + id
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    location.reload();
                } else {
                    alert('Error: ' + (data.message || 'Failed to mark as read'));
                }
            })
            .catch(error => {
                alert('Error marking as read');
                console.error(error);
            });
        }
    </script>
</body>
</html>