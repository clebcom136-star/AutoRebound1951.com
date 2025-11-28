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
                
                <a href="?tab=inventory" class="sidebar-item active flex items-center px-4 py-3 hover:bg-gray-800 transition">
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
                <a href="?tab=visitor-details" class="sidebar-item  flex items-center px-4 py-3 hover:bg-gray-800 transition">
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
                        Inventory                    </h2>
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
                                    


<!-- Inventory Tab - EXACTLY like old site -->

<div class="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700">

    <div class="p-6 border-b border-gray-100 dark:border-gray-700">

        <div class="flex items-center justify-between">

            <div>

                <h2 class="text-xl font-semibold text-gray-900 dark:text-white">Inventory Management</h2>

                <p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Total products: 20 | Filtered: 20</p>

            </div>

            <div class="flex gap-2">

                <button onclick="location.reload()" class="px-4 py-2 bg-orange-500 text-white rounded-lg hover:bg-orange-600 transition-colors">

                    Refresh

                </button>

                <button onclick="openAddVehicleModal()" class="px-4 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition-colors">

                    Add New Vehicle</button>
                <button onclick="deleteSelectedVehicles()" class="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors">
                    <i class="fas fa-trash mr-2"></i>Delete Selected
                </button>

            </div>

        </div>

    </div>

    

    

    <div class="p-6">

        <!-- Category Visibility Management -->

        <div class="mb-6 p-4 bg-gray-50 dark:bg-gray-900 rounded-lg">

            <h3 class="text-sm font-semibold text-gray-700 dark:text-gray-300 mb-3">Category Visibility:</h3>

            <div class="grid grid-cols-2 md:grid-cols-4 gap-3">

                
                <div class="flex items-center justify-between p-3 bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-600">

                    <div class="flex-1">

                        <div class="font-medium text-sm text-gray-900 dark:text-white">Cars &amp; Trucks</div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">11 products</div>

                    </div>

                    <form method="POST" action="?tab=inventory" style="display: inline;">

                        <input type="hidden" name="toggle_visibility" value="1">

                        <input type="hidden" name="category" value="cars-trucks">

                        <input type="hidden" name="visible" value="1">

                        <button type="submit" 

                                class="ml-2 px-3 py-1 text-xs font-medium rounded-full transition-colors bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200 hover:bg-gray-200 dark:hover:bg-gray-600">

                            OFF
                        </button>

                    </form>

                </div>

                
                <div class="flex items-center justify-between p-3 bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-600">

                    <div class="flex-1">

                        <div class="font-medium text-sm text-gray-900 dark:text-white">RVs &amp; Motorhomes</div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">7 products</div>

                    </div>

                    <form method="POST" action="?tab=inventory" style="display: inline;">

                        <input type="hidden" name="toggle_visibility" value="1">

                        <input type="hidden" name="category" value="rvs-motorhomes">

                        <input type="hidden" name="visible" value="1">

                        <button type="submit" 

                                class="ml-2 px-3 py-1 text-xs font-medium rounded-full transition-colors bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200 hover:bg-gray-200 dark:hover:bg-gray-600">

                            OFF
                        </button>

                    </form>

                </div>

                
                <div class="flex items-center justify-between p-3 bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-600">

                    <div class="flex-1">

                        <div class="font-medium text-sm text-gray-900 dark:text-white">Classic Cars</div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">1 products</div>

                    </div>

                    <form method="POST" action="?tab=inventory" style="display: inline;">

                        <input type="hidden" name="toggle_visibility" value="1">

                        <input type="hidden" name="category" value="classic-cars">

                        <input type="hidden" name="visible" value="1">

                        <button type="submit" 

                                class="ml-2 px-3 py-1 text-xs font-medium rounded-full transition-colors bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200 hover:bg-gray-200 dark:hover:bg-gray-600">

                            OFF
                        </button>

                    </form>

                </div>

                
                <div class="flex items-center justify-between p-3 bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-600">

                    <div class="flex-1">

                        <div class="font-medium text-sm text-gray-900 dark:text-white">Heavy Equipment</div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">1 products</div>

                    </div>

                    <form method="POST" action="?tab=inventory" style="display: inline;">

                        <input type="hidden" name="toggle_visibility" value="1">

                        <input type="hidden" name="category" value="heavy-equipment">

                        <input type="hidden" name="visible" value="1">

                        <button type="submit" 

                                class="ml-2 px-3 py-1 text-xs font-medium rounded-full transition-colors bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200 hover:bg-gray-200 dark:hover:bg-gray-600">

                            OFF
                        </button>

                    </form>

                </div>

                
            </div>

        </div>

        

        <!-- Category Filters - Show all categories regardless of visibility -->

        <div class="mb-4">

            <h3 class="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Filter by Category:</h3>

            <div class="flex flex-wrap gap-2">

                <button onclick="setCategoryFilter('all')" 

                        class="px-4 py-2 rounded-lg font-medium transition-colors border bg-gray-900 dark:bg-orange-600 text-white border-gray-900 dark:border-orange-600">

                    All Categories (20)

                </button>

                
                <button onclick="setCategoryFilter('cars-trucks')" 

                        class="px-4 py-2 rounded-lg font-medium transition-colors border bg-white dark:bg-gray-700 text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600 border-gray-200 dark:border-gray-600">

                    Cars &amp; Trucks (11)

                </button>

                
                <button onclick="setCategoryFilter('rvs-motorhomes')" 

                        class="px-4 py-2 rounded-lg font-medium transition-colors border bg-white dark:bg-gray-700 text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600 border-gray-200 dark:border-gray-600">

                    RVs &amp; Motorhomes (7)

                </button>

                
                <button onclick="setCategoryFilter('classic-cars')" 

                        class="px-4 py-2 rounded-lg font-medium transition-colors border bg-white dark:bg-gray-700 text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600 border-gray-200 dark:border-gray-600">

                    Classic Cars (1)

                </button>

                
                <button onclick="setCategoryFilter('heavy-equipment')" 

                        class="px-4 py-2 rounded-lg font-medium transition-colors border bg-white dark:bg-gray-700 text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600 border-gray-200 dark:border-gray-600">

                    Heavy Equipment (1)

                </button>

                
            </div>

        </div>

        

        <!-- Products Table - EXACTLY like old site -->

        <div class="overflow-hidden">

            <div class="overflow-x-auto">

                <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">

                    <thead class="bg-gray-50 dark:bg-gray-900">

                        <tr>

                            <th class="px-2 py-2 text-center">
                            <input type="checkbox" id="selectAllVehicles" onclick="toggleSelectAllVehicles(this)">
                        </th>
<th class="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">Product</th>

                            <th class="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">Category</th>

                            <th class="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">Price</th>

                            <th class="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">Status</th>

                            <th class="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">Views</th>

                            <th class="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">Clicks</th>

                            <th class="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">Featured</th>

                            <th class="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">Actions</th>

                        </tr>

                    </thead>

                    <tbody class="bg-white dark:bg-gray-800 divide-y divide-gray-200 dark:divide-gray-700">

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="106">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/K6HcpmO.jpeg"

                                             alt="1996 Dodge Roadtrek 190 Popular"

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            1996 Dodge Roadtrek 190 Popular
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK7642
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    RVs & Motorhomes
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $1,000
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-red-100 dark:bg-red-900 text-red-800 dark:text-red-200">

                                        Sold
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        93
                                    </span>

                                    <button onclick="resetCounter(106, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(106, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(106, true)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-gray-100 text-gray-600 hover:bg-gray-200" 

                                        title="Make featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Feature
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(106)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(106)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(106, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" >Available</option>

                                        <option value="reserved" >Reserved</option>

                                        <option value="sold" selected>Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="105">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/ZrR8N9m.jpeg"

                                             alt="1969 Chevrolet Camaro"

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            1969 Chevrolet Camaro
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK7512
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    Classic Cars
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $4,000
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-red-100 dark:bg-red-900 text-red-800 dark:text-red-200">

                                        Sold
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        23
                                    </span>

                                    <button onclick="resetCounter(105, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(105, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(105, true)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-gray-100 text-gray-600 hover:bg-gray-200" 

                                        title="Make featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Feature
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(105)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(105)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(105, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" >Available</option>

                                        <option value="reserved" >Reserved</option>

                                        <option value="sold" selected>Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="104">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/pqBm4oJ.jpeg"

                                             alt="2011 Honda Pilot Touring"

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            2011 Honda Pilot Touring
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK3832
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    Cars & Trucks
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $1,000
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-orange-100 dark:bg-orange-900 text-orange-800 dark:text-orange-200">

                                        Reserved
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        75
                                    </span>

                                    <button onclick="resetCounter(104, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(104, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(104, true)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-gray-100 text-gray-600 hover:bg-gray-200" 

                                        title="Make featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Feature
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(104)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(104)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(104, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" >Available</option>

                                        <option value="reserved" selected>Reserved</option>

                                        <option value="sold" >Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="103">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/OPSPDZ0.jpeg"

                                             alt="1996 Toyota Tacoma 4x4 extended cab pickup"

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            1996 Toyota Tacoma 4x4 extended cab pickup
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK2009
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    Cars & Trucks
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $500
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-orange-100 dark:bg-orange-900 text-orange-800 dark:text-orange-200">

                                        Reserved
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        231
                                    </span>

                                    <button onclick="resetCounter(103, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(103, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(103, false)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800 hover:bg-yellow-200" 

                                        title="Remove from featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Featured
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(103)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(103)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(103, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" >Available</option>

                                        <option value="reserved" selected>Reserved</option>

                                        <option value="sold" >Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="102">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/q5ONdUC.jpeg"

                                             alt="1991 Winnebago Warrior"

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            1991 Winnebago Warrior
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK9484
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    RVs & Motorhomes
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $1,500
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-red-100 dark:bg-red-900 text-red-800 dark:text-red-200">

                                        Sold
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        925
                                    </span>

                                    <button onclick="resetCounter(102, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(102, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(102, false)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800 hover:bg-yellow-200" 

                                        title="Remove from featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Featured
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(102)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(102)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(102, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" >Available</option>

                                        <option value="reserved" >Reserved</option>

                                        <option value="sold" selected>Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="101">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/rcjTLew.jpeg"

                                             alt="Bobcat s550  Enclosed cab"

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            Bobcat s550  Enclosed cab
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK2047
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    Heavy Equipment
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $3,000
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-red-100 dark:bg-red-900 text-red-800 dark:text-red-200">

                                        Sold
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        80
                                    </span>

                                    <button onclick="resetCounter(101, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(101, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(101, false)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800 hover:bg-yellow-200" 

                                        title="Remove from featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Featured
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(101)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(101)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(101, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" >Available</option>

                                        <option value="reserved" >Reserved</option>

                                        <option value="sold" selected>Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="100">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/qLc4xT4.jpeg"

                                             alt="2005 honda goldwing 1800"

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            2005 honda goldwing 1800
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK2428
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    Cars & Trucks
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $1,000
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-orange-100 dark:bg-orange-900 text-orange-800 dark:text-orange-200">

                                        Reserved
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        198
                                    </span>

                                    <button onclick="resetCounter(100, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(100, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(100, false)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800 hover:bg-yellow-200" 

                                        title="Remove from featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Featured
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(100)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(100)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(100, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" >Available</option>

                                        <option value="reserved" selected>Reserved</option>

                                        <option value="sold" >Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="99">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/7yzJvbH.jpeg"

                                             alt="2007 Airstream Safari Sport 3000"

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            2007 Airstream Safari Sport 3000
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK1085
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    RVs & Motorhomes
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $1,000
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-orange-100 dark:bg-orange-900 text-orange-800 dark:text-orange-200">

                                        Reserved
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        60
                                    </span>

                                    <button onclick="resetCounter(99, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(99, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(99, false)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800 hover:bg-yellow-200" 

                                        title="Remove from featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Featured
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(99)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(99)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(99, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" >Available</option>

                                        <option value="reserved" selected>Reserved</option>

                                        <option value="sold" >Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="98">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/6xAcWoG.jpeg"

                                             alt="2011 Volkswagen Tiguan SEL 4Motion 2.0T AWD [44K Miles]"

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            2011 Volkswagen Tiguan SEL 4Motion 2.0T AWD [44K Miles]
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK5255
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    Cars & Trucks
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $1,500
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-red-100 dark:bg-red-900 text-red-800 dark:text-red-200">

                                        Sold
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        52
                                    </span>

                                    <button onclick="resetCounter(98, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(98, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(98, false)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800 hover:bg-yellow-200" 

                                        title="Remove from featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Featured
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(98)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(98)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(98, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" >Available</option>

                                        <option value="reserved" >Reserved</option>

                                        <option value="sold" selected>Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="97">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/yviP42l.jpeg"

                                             alt="2012 Buick Enclave Convenience Sport Utility"

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            2012 Buick Enclave Convenience Sport Utility
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK4186
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    Cars & Trucks
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $1,000
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-orange-100 dark:bg-orange-900 text-orange-800 dark:text-orange-200">

                                        Reserved
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        217
                                    </span>

                                    <button onclick="resetCounter(97, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(97, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(97, false)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800 hover:bg-yellow-200" 

                                        title="Remove from featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Featured
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(97)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(97)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(97, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" >Available</option>

                                        <option value="reserved" selected>Reserved</option>

                                        <option value="sold" >Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="96">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/l5eiW7j.jpeg"

                                             alt="2008 "

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            2008 
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK4135
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    RVs & Motorhomes
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $1,000
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-red-100 dark:bg-red-900 text-red-800 dark:text-red-200">

                                        Sold
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        67
                                    </span>

                                    <button onclick="resetCounter(96, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(96, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(96, false)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800 hover:bg-yellow-200" 

                                        title="Remove from featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Featured
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(96)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(96)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(96, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" >Available</option>

                                        <option value="reserved" >Reserved</option>

                                        <option value="sold" selected>Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="95">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/zk2oI3R.jpeg"

                                             alt="2004 FORD F-150 LIGHTNING SVT"

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            2004 FORD F-150 LIGHTNING SVT
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK5953
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    Cars & Trucks
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $1,500
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-orange-100 dark:bg-orange-900 text-orange-800 dark:text-orange-200">

                                        Reserved
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        224
                                    </span>

                                    <button onclick="resetCounter(95, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(95, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(95, false)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800 hover:bg-yellow-200" 

                                        title="Remove from featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Featured
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(95)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(95)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(95, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" >Available</option>

                                        <option value="reserved" selected>Reserved</option>

                                        <option value="sold" >Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="94">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/ZKt7vbo.jpeg"

                                             alt="1995 Airstream Excella Classic 25"

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            1995 Airstream Excella Classic 25
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK6332
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    RVs & Motorhomes
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $800
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-orange-100 dark:bg-orange-900 text-orange-800 dark:text-orange-200">

                                        Reserved
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        46
                                    </span>

                                    <button onclick="resetCounter(94, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(94, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(94, false)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800 hover:bg-yellow-200" 

                                        title="Remove from featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Featured
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(94)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(94)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(94, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" >Available</option>

                                        <option value="reserved" selected>Reserved</option>

                                        <option value="sold" >Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="93">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/ZJmAbs1.jpeg"

                                             alt="1993 Fleetwood Jamboree Searcher"

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            1993 Fleetwood Jamboree Searcher
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK8225
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    RVs & Motorhomes
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $800
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-red-100 dark:bg-red-900 text-red-800 dark:text-red-200">

                                        Sold
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        176
                                    </span>

                                    <button onclick="resetCounter(93, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(93, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(93, false)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800 hover:bg-yellow-200" 

                                        title="Remove from featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Featured
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(93)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(93)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(93, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" >Available</option>

                                        <option value="reserved" >Reserved</option>

                                        <option value="sold" selected>Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="72">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/QskCOHy.jpeg"

                                             alt="2008 Jaguar S-Type 3.0"

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            2008 Jaguar S-Type 3.0
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK5879
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    Cars & Trucks
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $1,000
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200">

                                        Available
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        72
                                    </span>

                                    <button onclick="resetCounter(72, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(72, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(72, false)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800 hover:bg-yellow-200" 

                                        title="Remove from featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Featured
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(72)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(72)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(72, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" selected>Available</option>

                                        <option value="reserved" >Reserved</option>

                                        <option value="sold" >Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="71">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/b9UP3bj.jpeg"

                                             alt="2006 Honda Accord LX"

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            2006 Honda Accord LX
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK7368
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    Cars & Trucks
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $800
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200">

                                        Available
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        166
                                    </span>

                                    <button onclick="resetCounter(71, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(71, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(71, false)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800 hover:bg-yellow-200" 

                                        title="Remove from featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Featured
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(71)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(71)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(71, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" selected>Available</option>

                                        <option value="reserved" >Reserved</option>

                                        <option value="sold" >Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="70">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/7obQC4w.jpeg"

                                             alt="2005 Toyota Tacoma Access Cab"

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            2005 Toyota Tacoma Access Cab
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK6398
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    Cars & Trucks
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $1,500
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200">

                                        Available
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        29
                                    </span>

                                    <button onclick="resetCounter(70, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(70, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(70, true)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-gray-100 text-gray-600 hover:bg-gray-200" 

                                        title="Make featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Feature
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(70)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(70)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(70, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" selected>Available</option>

                                        <option value="reserved" >Reserved</option>

                                        <option value="sold" >Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="69">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/FPmLGkS.jpeg"

                                             alt="2005 Lexus ES 330"

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            2005 Lexus ES 330
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK3967
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    Cars & Trucks
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $800
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200">

                                        Available
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        75
                                    </span>

                                    <button onclick="resetCounter(69, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(69, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(69, true)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-gray-100 text-gray-600 hover:bg-gray-200" 

                                        title="Make featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Feature
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(69)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(69)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(69, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" selected>Available</option>

                                        <option value="reserved" >Reserved</option>

                                        <option value="sold" >Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="67">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/nupgOuI.jpeg"

                                             alt="2003 Ford E-450 Class C Sunseeker 24ft"

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            2003 Ford E-450 Class C Sunseeker 24ft
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK3005
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    RVs & Motorhomes
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $1,500
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200">

                                        Available
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        320
                                    </span>

                                    <button onclick="resetCounter(67, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(67, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(67, false)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800 hover:bg-yellow-200" 

                                        title="Remove from featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Featured
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(67)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(67)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(67, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" selected>Available</option>

                                        <option value="reserved" >Reserved</option>

                                        <option value="sold" >Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                        <tr class="hover:bg-gray-50 dark:hover:bg-gray-700">
                            <td class="px-2 py-2 text-center">
                                <input type="checkbox" class="vehicle-checkbox" value="65">
                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center">

                                    <div class="flex-shrink-0 h-10 w-10">

                                        
                                        <img class="h-10 w-10 rounded object-cover"

                                             src="https://i.imgur.com/xBpfp4t.jpeg"

                                             alt="2003 CHEVROLET TAHOE C1500"

                                             onerror="this.src='https://via.placeholder.com/150x150?text=Error'">

                                    </div>

                                    <div class="ml-3">

                                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                                            2003 CHEVROLET TAHOE C1500
                                        </div>

                                        <div class="text-xs text-gray-500 dark:text-gray-400">

                                            #STK2998
                                        </div>

                                    </div>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <span class="inline-flex px-1 py-0.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200">

                                    Cars & Trucks
                                </span>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="text-xs font-medium text-gray-900">

                                    $800
                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex flex-col gap-1">

                                    <span class="inline-flex px-2 py-0.5 text-xs font-semibold rounded bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200">

                                        Available
                                    </span>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        74
                                    </span>

                                    <button onclick="resetCounter(65, 'views')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset views">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <div class="flex items-center space-x-1">

                                    <span class="text-xs font-medium text-gray-900">

                                        0
                                    </span>

                                    <button onclick="resetCounter(65, 'inquiries')" 

                                            class="text-xs text-gray-500 hover:text-red-600" 

                                            title="Reset buy clicks">

                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 

                                                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />

                                        </svg>

                                    </button>

                                </div>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap">

                                <button onclick="toggleFeatured(65, true)" 

                                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-gray-100 text-gray-600 hover:bg-gray-200" 

                                        title="Make featured">

                                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 24 24">

                                        <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" />

                                    </svg>

                                    Feature
                                </button>

                            </td>

                            <td class="px-3 py-2 whitespace-nowrap text-sm font-medium">

                                <div class="flex items-center space-x-2">

                                    <button onclick="editVehicle(65)" 

                                            class="text-orange-500 hover:text-blue-900 text-xs">

                                        Edit

                                    </button>

                                    <button onclick="deleteVehicle(65)" 

                                            class="text-red-600 hover:text-red-900 text-xs">

                                        Delete

                                    </button>

                                    <select onchange="updateStatus(65, this.value)"

                                            class="text-xs border border-gray-300 rounded px-1 py-0.5">

                                        <option value="available" selected>Available</option>

                                        <option value="reserved" >Reserved</option>

                                        <option value="sold" >Sold</option>

                                    </select>

                                </div>

                            </td>

                        </tr>

                        
                    </tbody>

                </table>

            </div>

        </div>

        

        
    </div>

</div>



<!-- Edit Vehicle Modal -->

<div id="editVehicleModal" class="hidden fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">

    <div class="bg-white rounded-lg max-w-4xl w-full max-h-[90vh] overflow-y-auto">

        <div class="sticky top-0 bg-white border-b px-6 py-4 flex justify-between items-center">

            <h2 class="text-xl font-bold">Edit Vehicle</h2>

            <button onclick="closeEditVehicleModal()" class="text-gray-500 hover:text-gray-700">

                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>

                </svg>

            </button>

        </div>

        

        <form id="editVehicleForm" class="p-6">

            <input type="hidden" id="editVehicleId" name="id">

            <div class="grid grid-cols-2 gap-6">

                <!-- Basic Info -->

                <div class="col-span-2">

                    <h3 class="font-semibold text-gray-700 mb-3">Basic Information</h3>

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Vehicle Name *</label>

                    <input type="text" id="editName" name="name" required class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Category *</label>

                    <select id="editCategory" name="category" required class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                        
                        <option value="cars-trucks">Cars &amp; Trucks</option>

                        
                        <option value="rvs-motorhomes">RVs &amp; Motorhomes</option>

                        
                        <option value="classic-cars">Classic Cars</option>

                        
                        <option value="heavy-equipment">Heavy Equipment</option>

                        
                    </select>

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Price *</label>

                    <input type="number" id="editPrice" name="price" required class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Year</label>

                    <input type="number" id="editYear" name="year" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Make</label>

                    <input type="text" id="editMake" name="make" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Model</label>

                    <input type="text" id="editModel" name="model" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                </div>

                

                <!-- Vehicle Details -->

                <div class="col-span-2 mt-4">

                    <h3 class="font-semibold text-gray-700 mb-3">Vehicle Details</h3>

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Mileage</label>

                    <input type="number" id="editMileage" name="mileage" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Engine</label>

                    <input type="text" id="editEngine" name="engine" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Transmission</label>

                    <select id="editTransmission" name="transmission" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                        <option value="">Select...</option>

                        <option value="automatic">Automatic</option>

                        <option value="manual">Manual</option>

                        <option value="cvt">CVT</option>

                    </select>

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Fuel Type</label>

                    <select id="editFuelType" name="fuel_type" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                        <option value="">Select...</option>

                        <option value="gasoline">Gasoline</option>

                        <option value="diesel">Diesel</option>

                        <option value="hybrid">Hybrid</option>

                        <option value="electric">Electric</option>

                    </select>

                </div>



                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Drivetrain</label>

                    <select id="editDrivetrain" name="drivetrain" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                        <option value="fwd">FWD (Front-Wheel Drive)</option>

                        <option value="rwd">RWD (Rear-Wheel Drive)</option>

                        <option value="awd">AWD (All-Wheel Drive)</option>

                        <option value="4wd">4WD (Four-Wheel Drive)</option>

                    </select>

                </div>



                <div class="col-span-2">

                    <label class="block text-sm font-medium text-gray-700 mb-1">Description</label>

                    <textarea id="editDescription" name="description" rows="4" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500"></textarea>

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Status</label>

                    <select id="editStatus" name="status" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                        <option value="available">Available</option>

                        <option value="reserved">Reserved</option>

                        <option value="sold">Sold</option>

                    </select>

                </div>



                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">

                        Payment Method Allowed

                        <span class="text-orange-500">*</span>

                    </label>

                    <select id="editPaymentMethod" name="payment_method_allowed" required class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                        <option value="both">

                            <i class="fas fa-coins mr-1"></i>

                            Auto (Based on Price)

                        </option>

                        <option value="wire_transfer">

                            <i class="fas fa-university mr-1"></i>

                            Wire Transfer Only

                        </option>

                        <option value="card">

                            <i class="fab fa-apple-pay mr-1"></i>

                            Apple Pay Only

                        </option>

                    </select>

                    <p class="text-xs text-gray-500 mt-1">

                        <i class="fas fa-info-circle"></i>

                        Auto: <$5,000 = Apple Pay, ≥$5,000 = Wire Transfer

                    </p>

                </div>



                <div class="col-span-2">

                    <label class="flex items-center space-x-2">

                        <input type="checkbox" id="editFeatured" name="featured" class="rounded text-orange-500 focus:ring-orange-500">

                        <span class="text-sm font-medium text-gray-700">Featured Vehicle</span>

                    </label>

                </div>

            </div>

            

            <div class="flex justify-end gap-3 mt-6">

                <button type="button" onclick="closeEditVehicleModal()" class="px-6 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50">

                    Cancel

                </button>

                <button type="submit" class="px-6 py-2 bg-orange-500 text-white rounded-lg hover:bg-orange-600">

                    Update Vehicle

                </button>

            </div>

        </form>

    </div>

</div>



<!-- Add Vehicle Modal -->

<div id="addVehicleModal" class="hidden fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">

    <div class="bg-white rounded-lg max-w-4xl w-full max-h-[90vh] overflow-y-auto">

        <div class="sticky top-0 bg-white border-b px-6 py-4 flex justify-between items-center">

            <h2 class="text-xl font-bold">Add New Vehicle</h2>

            <button onclick="closeAddVehicleModal()" class="text-gray-500 hover:text-gray-700">

                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>

                </svg>

            </button>

        </div>

        

        <form id="addVehicleForm" class="p-6">

            <div class="grid grid-cols-2 gap-6">

                <!-- Basic Info -->

                <div class="col-span-2">

                    <h3 class="font-semibold text-gray-700 mb-3">Basic Information</h3>

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Vehicle Name *</label>

                    <input type="text" name="name" required class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">VIN *</label>

                    <input type="text" name="vin" required class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Year *</label>

                    <input type="number" name="year" required min="1900" max="2030" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Make *</label>

                    <input type="text" name="make" required class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Model *</label>

                    <input type="text" name="model" required class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Trim Level</label>

                    <input type="text" name="trim_level" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                </div>

                

                <!-- Pricing -->

                <div class="col-span-2">

                    <h3 class="font-semibold text-gray-700 mb-3 mt-4">Pricing</h3>

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Price *</label>

                    <input type="number" name="price" required step="0.01" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Original Price</label>

                    <input type="number" name="original_price" step="0.01" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                </div>

                

                <!-- Vehicle Details -->

                <div class="col-span-2">

                    <h3 class="font-semibold text-gray-700 mb-3 mt-4">Vehicle Details</h3>

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Mileage *</label>

                    <input type="number" name="mileage" required class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Category *</label>

                    <select name="category" required class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                        <option value="">Select Category</option>

                        
                        <option value="cars-trucks">Cars &amp; Trucks</option>

                        
                        <option value="rvs-motorhomes">RVs &amp; Motorhomes</option>

                        
                        <option value="classic-cars">Classic Cars</option>

                        
                        <option value="heavy-equipment">Heavy Equipment</option>

                        
                    </select>

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Condition</label>

                    <select name="condition_type" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                        <option value="used">Used</option>

                        <option value="new">New</option>

                        <option value="certified">Certified</option>

                    </select>

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Status</label>

                    <select name="status" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                        <option value="available">Available</option>

                        <option value="reserved">Reserved</option>

                        <option value="sold">Sold</option>

                    </select>

                </div>



                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">

                        Payment Method Allowed

                        <span class="text-orange-500">*</span>

                    </label>

                    <select name="payment_method_allowed" required class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                        <option value="both" selected>

                            <i class="fas fa-coins mr-1"></i>

                            Auto (Based on Price)

                        </option>

                        <option value="wire_transfer">

                            <i class="fas fa-university mr-1"></i>

                            Wire Transfer Only

                        </option>

                        <option value="card">

                            <i class="fab fa-apple-pay mr-1"></i>

                            Apple Pay Only

                        </option>

                    </select>

                    <p class="text-xs text-gray-500 mt-1">

                        <i class="fas fa-info-circle"></i>

                        Auto: <$5,000 = Apple Pay, ≥$5,000 = Wire Transfer

                    </p>

                </div>



                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Exterior Color</label>

                    <input type="text" name="exterior_color" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Interior Color</label>

                    <input type="text" name="interior_color" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Engine</label>

                    <input type="text" name="engine" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                </div>

                

                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Transmission</label>

                    <select name="transmission" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                        <option value="automatic">Automatic</option>

                        <option value="manual">Manual</option>

                        <option value="cvt">CVT</option>

                    </select>

                </div>



                <div>

                    <label class="block text-sm font-medium text-gray-700 mb-1">Drivetrain</label>

                    <select name="drivetrain" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                        <option value="fwd">FWD (Front-Wheel Drive)</option>

                        <option value="rwd">RWD (Rear-Wheel Drive)</option>

                        <option value="awd">AWD (All-Wheel Drive)</option>

                        <option value="4wd">4WD (Four-Wheel Drive)</option>

                    </select>

                </div>



                <!-- Images -->

                <div class="col-span-2">

                    <h3 class="font-semibold text-gray-700 mb-3 mt-4">Images</h3>

                </div>

                

                <div class="col-span-2">

                    <label class="block text-sm font-medium text-gray-700 mb-1">Thumbnail Image (Main Image)</label>

                    <input type="text" name="main_image" placeholder="https://i.imgur.com/tOm07gE.jpg" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                    <p class="text-xs text-gray-500 mt-1">✅ Use DIRECT IMAGE URL for main thumbnail</p>

                    <p class="text-xs text-gray-500">Example: https://i.imgur.com/tOm07gE.jpg</p>

                </div>



                <div class="col-span-2">

                    <label class="block text-sm font-medium text-gray-700 mb-1">Gallery Images (Multiple URLs)</label>

                    <textarea name="images" rows="3" placeholder="Add multiple image URLs, one per line or comma separated" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500"></textarea>

                    <p class="text-xs text-gray-500 mt-1">✅ Add direct image URLs (one per line or comma separated)</p>

                    <p class="text-xs text-gray-500">Example:<br>

                    https://i.imgur.com/image1.jpg<br>

                    https://i.imgur.com/image2.jpg<br>

                    https://i.imgur.com/image3.jpg</p>

                </div>



                <!-- Description -->

                <div class="col-span-2">

                    <label class="block text-sm font-medium text-gray-700 mb-1">Description</label>

                    <textarea name="description" rows="4" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500"></textarea>

                </div>

                

                <!-- Featured -->

                <div class="col-span-2">

                    <label class="flex items-center">

                        <input type="checkbox" name="featured" class="mr-2">

                        <span class="text-sm font-medium text-gray-700">Featured Vehicle</span>

                    </label>

                </div>

            </div>

            

            <div class="flex justify-end gap-3 mt-6">

                <button type="button" onclick="closeAddVehicleModal()" class="px-6 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50">

                    Cancel

                </button>

                <button type="submit" class="px-6 py-2 bg-orange-500 text-white rounded-lg hover:bg-orange-600">

                    Add Vehicle

                </button>

            </div>

        </form>

    </div>

</div>



<script>

// Filter functions - EXACTLY like old site

function setCategoryFilter(category) {

    const params = new URLSearchParams(window.location.search);

    params.set('tab', 'inventory');

    params.set('category', category);

    window.location.search = params.toString();

}



function openAddVehicleModal() {

    document.getElementById('addVehicleModal').classList.remove('hidden');

}



function closeAddVehicleModal() {

    document.getElementById('addVehicleModal').classList.add('hidden');

    document.getElementById('addVehicleForm').reset();

}



function editVehicle(id) {

    // Fetch vehicle data

    fetch('/api/admin/get-vehicle.php?id=' + id)

    .then(response => response.json())

    .then(data => {

        if (data.success) {

            const vehicle = data.vehicle;

            // Populate form fields

            document.getElementById('editVehicleId').value = vehicle.id;

            document.getElementById('editName').value = vehicle.name || '';

            document.getElementById('editCategory').value = vehicle.category || 'cars-trucks';

            document.getElementById('editPrice').value = vehicle.price || '';

            document.getElementById('editYear').value = vehicle.year || '';

            document.getElementById('editMake').value = vehicle.make || '';

            document.getElementById('editModel').value = vehicle.model || '';

            document.getElementById('editMileage').value = vehicle.mileage || '';

            document.getElementById('editEngine').value = vehicle.engine || '';

            document.getElementById('editTransmission').value = vehicle.transmission || '';

            document.getElementById('editFuelType').value = vehicle.fuel_type || '';

            document.getElementById('editDrivetrain').value = vehicle.drivetrain || 'fwd';

            document.getElementById('editDescription').value = vehicle.description || '';

            document.getElementById('editStatus').value = vehicle.status || 'available';

            document.getElementById('editPaymentMethod').value = vehicle.payment_method_allowed || 'both';

            document.getElementById('editFeatured').checked = vehicle.featured == 1;

            

            // Show modal

            document.getElementById('editVehicleModal').classList.remove('hidden');

        } else {

            alert('Error loading vehicle data');

        }

    })

    .catch(error => {

        alert('Error loading vehicle data');

        console.error(error);

    });

}



function closeEditVehicleModal() {

    document.getElementById('editVehicleModal').classList.add('hidden');

    document.getElementById('editVehicleForm').reset();

}



function deleteVehicle(id) {
    console.log('deleteVehicle called:', id);
    console.log('Type of ID:', typeof id);
    console.log('parseInt(id):', parseInt(id));

    
    if (confirm('Are you sure you want to delete this vehicle?')) {
        // Use GET method directly
        fetch('/api/admin/delete-vehicle.php?id=' + parseInt(id), {
            method: 'GET',
            credentials: 'same-origin'
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                location.reload();
            } else {
                alert('Error deleting vehicle: ' + (data.message || 'Unknown error'));
            }
        })
        .catch(error => {
            console.error('Delete error:', error);
            alert('Error deleting vehicle. Check console for details.');
        });
    }
}



function toggleFeatured(id, featured) {

    console.log('toggleFeatured called:', id, featured);

    // Convert string to boolean

    const featuredBool = featured === true || featured === 'true';

    console.log('Sending featured as:', featuredBool);



    // Since server converts POST to GET, send as URL parameters

    fetch('/api/admin/update-vehicle-featured.php?id=' + id + '&featured=' + featuredBool, {

        method: 'GET',
        credentials: 'same-origin'

    })

    .then(response => response.json())

    .then(data => {

        if (data.success) {

            location.reload();

        } else {

            alert('Error: ' + data.message);

        }

    })

    .catch(error => {

        console.error('Error:', error);

        alert('Error updating featured status');

    });

}



function updateStatus(id, status) {

    console.log('updateStatus called:', id, status);

    // Since server converts POST to GET, send as URL parameters

    fetch('/api/admin/update-vehicle.php?id=' + id + '&status=' + status, {

        method: 'GET',
        credentials: 'same-origin'

    })

    .then(response => {

        if (!response.ok) {

            throw new Error('Network response was not ok');

        }

        return response.json();

    })

    .then(data => {

        if (data.success) {

            console.log('Status updated successfully:', data.message);

            // Show success message

            const alertDiv = document.createElement('div');

            alertDiv.className = 'fixed top-4 right-4 bg-green-500 text-white px-4 py-2 rounded shadow-lg z-50';

            alertDiv.textContent = 'Status updated successfully';

            document.body.appendChild(alertDiv);

            setTimeout(() => alertDiv.remove(), 3000);

        } else {

            alert('Error updating status: ' + (data.message || 'Unknown error'));

            location.reload();

        }

    })

    .catch(error => {

        console.error('Error:', error);

        alert('Error updating status: ' + error.message);

        location.reload();

    });

}



function resetCounter(id, type) {

    console.log('resetCounter called:', id, type);

    if (!confirm(`Are you sure you want to reset ${type} counter?`)) {

        return;

    }

    

    fetch('/api/admin/reset-counter.php?id=' + id + '&type=' + type, {

        method: 'POST',
        credentials: 'same-origin',

        headers: {'Content-Type': 'application/json'},

        body: JSON.stringify({id: id, type: type})

    })

    .then(response => response.json())

    .then(data => {

        if (data.success) {

            location.reload();

        } else {

            alert('Error resetting counter');

        }

    });

}



// Removed AJAX function - using simple PHP form submit instead



// Handle edit vehicle form

document.getElementById('editVehicleForm').addEventListener('submit', function(e) {

    e.preventDefault();



    const formData = new FormData(this);



    // Convert FormData to URL parameters

    const params = new URLSearchParams();

    for (let [key, value] of formData.entries()) {

        if (key === 'featured') {

            params.append(key, formData.get('featured') ? 'true' : 'false');

        } else {

            params.append(key, value);

        }

    }



    // Since server converts POST to GET, send as URL parameters

    fetch('/api/admin/update-vehicle.php?' + params.toString(), {

        method: 'GET',
        credentials: 'same-origin'

    })

    .then(response => response.json())

    .then(result => {

        if (result.success) {

            alert('Vehicle updated successfully!');

            location.reload();

        } else {

            alert('Error updating vehicle: ' + (result.message || 'Unknown error'));

        }

    })

    .catch(error => {

        alert('Error updating vehicle');

        console.error(error);

    });

});



// Handle add vehicle form

document.getElementById('addVehicleForm').addEventListener('submit', function(e) {

    e.preventDefault();



    const formData = new FormData(this);



    // Convert FormData to URL parameters

    const params = new URLSearchParams();

    for (let [key, value] of formData.entries()) {

        params.append(key, value);

    }



    // Debug: Log what we're sending

    console.log('Sending vehicle data:');

    console.log('URL parameters:', params.toString());



    // Since server converts POST to GET, send as URL parameters

    fetch('/api/admin/add-vehicle.php?' + params.toString(), {

        method: 'GET',
        credentials: 'same-origin'

    })

    .then(response => response.json())

    .then(data => {

        console.log('Response:', data);

        if (data.success) {

            alert('Vehicle added successfully!');

            location.reload();

        } else {

            alert('Error adding vehicle: ' + data.message);

        }

    })

    .catch(error => {

        console.error('Error:', error);

        alert('Error adding vehicle. Check console for details.');

    });

});



// Add console logging for debugging

console.log('Inventory JavaScript loaded');



// Check if functions are defined

const requiredFunctions = ['updateStatus', 'toggleFeatured', 'resetCounter', 'editVehicle', 'deleteVehicle'];

requiredFunctions.forEach(func => {

    if (typeof window[func] === 'function') {

        console.log(`✓ ${func} is defined`);

    } else {

        console.error(`✗ ${func} is NOT defined`);

    }

});


// Bulk delete functions for vehicles
function toggleSelectAllVehicles(source) {
    const checkboxes = document.querySelectorAll('.vehicle-checkbox');
    checkboxes.forEach(checkbox => {
        checkbox.checked = source.checked;
    });
}

function deleteSelectedVehicles() {
    const checkboxes = document.querySelectorAll('.vehicle-checkbox:checked');
    const selectedIds = Array.from(checkboxes).map(cb => cb.value);

    if (selectedIds.length === 0) {
        alert('Please select at least one vehicle to delete');
        return;
    }

    if (confirm('Are you sure you want to delete ' + selectedIds.length + ' vehicle(s)?')) {
        fetch('/api/admin/delete-vehicles.php?ids=' + selectedIds.join(','), {
            method: 'GET',
            credentials: 'same-origin'
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
            alert('Error deleting vehicles');
            console.error(error);
        });
    }
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