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
                
                <a href="?tab=orders" class="sidebar-item active flex items-center px-4 py-3 hover:bg-gray-800 transition">
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
                        Orders                    </h2>
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
                                    


<!-- Orders & Tracking Management -->

<div class="bg-white dark:bg-gray-800 rounded-lg shadow">

    <!-- Header with Stats -->

    <div class="px-6 py-4 border-b border-gray-200 dark:border-gray-700">

        <h3 class="text-lg font-semibold text-gray-800 dark:text-gray-200 mb-4">Orders & Tracking Management</h3>



        <!-- Stats Cards -->

        <div class="grid grid-cols-5 gap-4 mb-4">

            <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-3">

                <div class="text-2xl font-bold text-gray-900 dark:text-white">7</div>

                <div class="text-xs text-gray-600 dark:text-gray-400">Total Orders (30d)</div>

            </div>

            <div class="bg-yellow-50 dark:bg-yellow-900 rounded-lg p-3">

                <div class="text-2xl font-bold text-yellow-600 dark:text-yellow-400">6</div>

                <div class="text-xs text-gray-600 dark:text-gray-400">Pending</div>

            </div>

            <div class="bg-blue-50 dark:bg-blue-900 rounded-lg p-3">

                <div class="text-2xl font-bold text-blue-600 dark:text-blue-400">1</div>

                <div class="text-xs text-gray-600 dark:text-gray-400">Processing</div>

            </div>

            <div class="bg-indigo-50 dark:bg-indigo-900 rounded-lg p-3">

                <div class="text-2xl font-bold text-indigo-600 dark:text-indigo-400">0</div>

                <div class="text-xs text-gray-600 dark:text-gray-400">Shipping</div>

            </div>

            <div class="bg-green-50 dark:bg-green-900 rounded-lg p-3">

                <div class="text-2xl font-bold text-green-600 dark:text-green-400">0</div>

                <div class="text-xs text-gray-600 dark:text-gray-400">Completed</div>

            </div>

        </div>

    </div>



    <!-- Filters -->

    <div class="px-6 py-4 border-b border-gray-200 dark:border-gray-700 bg-gray-50 dark:bg-gray-900">

        <form method="GET" class="flex flex-wrap gap-4">

            <input type="hidden" name="tab" value="orders">



            <!-- Search -->

            <input type="text" name="searchOrder" placeholder="Search by order #, customer, email, or tracking #..."

                   value=""

                   class="flex-1 min-w-[300px] px-4 py-2 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-gray-900 dark:text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">



            <!-- Status Filter -->

            <select name="orderStatus" class="px-4 py-2 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-gray-900 dark:text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                <option value="all">All Status</option>

                <optgroup label="Active Orders">

                    <option value="pending" >Pending Payment</option>

                    <option value="payment_received" >Payment Confirmed</option>

                    <option value="processing" >Processing</option>

                    <option value="preparing" >Preparing</option>

                    <option value="ready" >Ready to Ship</option>

                    <option value="in_transit" >In Transit</option>

                </optgroup>

                <optgroup label="Completed">

                    <option value="delivered" >Delivered</option>

                    <option value="completed" >Completed</option>

                </optgroup>

                <optgroup label="Cancelled">

                    <option value="cancelled" >Cancelled</option>

                    <option value="refunded" >Refunded</option>

                </optgroup>

            </select>



            <!-- Date Filter -->

            <select name="dateFilter" class="px-4 py-2 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-gray-900 dark:text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                <option value="all">All Time</option>

                <option value="today" >Today</option>

                <option value="week" >Last 7 Days</option>

                <option value="month" >Last 30 Days</option>

            </select>



            <button type="submit" class="px-6 py-2 bg-gray-700 dark:bg-gray-600 text-white rounded-lg hover:bg-gray-800 dark:hover:bg-gray-700">

                Filter

            </button>



            
        </form>

    </div>



    <!-- Orders Table -->

    <div class="overflow-x-auto">

        
        <!-- Delete Selected Button -->

        <div class="px-6 py-3 bg-gray-50 dark:bg-gray-900 border-b border-gray-200 dark:border-gray-700 flex justify-between items-center">

            <div class="flex items-center space-x-4">

                <input type="checkbox" id="selectAll" class="rounded border-gray-300 dark:border-gray-600" onchange="toggleSelectAll()">

                <label for="selectAll" class="text-sm text-gray-700 dark:text-gray-300">Select All</label>

            </div>

            <button onclick="deleteSelectedOrders()" class="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 disabled:opacity-50" id="deleteSelectedBtn" disabled>

                Delete Selected

            </button>

        </div>



        <table class="w-full min-w-[1400px]">

            <thead class="bg-gray-50 dark:bg-gray-900">

                <tr>

                    <th class="w-10 px-2 py-3 text-center">

                        <span class="sr-only">Select</span>

                    </th>

                    <th class="w-32 px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider whitespace-nowrap">Order</th>

                    <th class="w-40 px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider whitespace-nowrap">Customer</th>

                    <th class="w-48 px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider whitespace-nowrap">Vehicle</th>

                    <th class="w-24 px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider whitespace-nowrap">Amount</th>

                    <th class="w-32 px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider whitespace-nowrap">Vehicle<br>Status</th>

                    <th class="w-36 px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider whitespace-nowrap">Order<br>Status</th>

                    <th class="w-32 px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider whitespace-nowrap">Tracking</th>

                    <th class="w-24 px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider whitespace-nowrap">Date</th>

                    <th class="w-36 px-4 py-3 text-center text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider whitespace-nowrap">Actions</th>

                </tr>

            </thead>

            <tbody class="bg-white dark:bg-gray-800 divide-y divide-gray-200 dark:divide-gray-700">

                
                <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 align-middle">

                    <!-- Checkbox -->

                    <td class="w-10 px-2 py-3 text-center">

                        <input type="checkbox" class="order-checkbox rounded border-gray-300 dark:border-gray-600" value="57" onchange="checkSelectedOrders()">

                    </td>



                    <!-- Order -->

                    <td class="w-32 px-4 py-3">

                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                            APL-20251127-6BD220
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">ID: 57</div>

                    </td>



                    <!-- Customer -->

                    <td class="w-40 px-4 py-3">

                        <div class="text-xs">

                            <div class="font-medium text-gray-900 dark:text-white truncate"> </div>

                            <div class="text-gray-500 dark:text-gray-400 truncate">simpl128213@gmail.com</div>

                        </div>

                    </td>



                    <!-- Vehicle -->

                    <td class="w-48 px-4 py-3">

                        <div class="flex items-center">

                            
                                <img src="https://i.imgur.com/xBpfp4t.jpeg"

                                     alt="Vehicle"

                                     class="w-12 h-9 object-cover rounded mr-2 flex-shrink-0"

                                     onerror="this.style.display='none'">

                            
                            <div class="min-w-0">

                                <div class="text-xs font-medium text-gray-900 dark:text-white truncate">

                                    2003 CHEVROLET TAHOE C1500
                                </div>

                                <div class="text-xs text-gray-500 dark:text-gray-400">VIN: 143110</div>

                            </div>

                        </div>

                    </td>



                    <!-- Amount -->

                    <td class="w-24 px-4 py-3">

                        <div class="text-xs font-semibold text-gray-900 dark:text-white">

                            $800
                        </div>

                        
                    </td>



                    <!-- Vehicle Status -->

                    <td class="w-32 px-4 py-3">

                        <select onchange="updateVehicleStatus(57, this.value)"

                                class="w-full text-xs px-2 py-1 rounded border

                                bg-yellow-50 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-200 border-yellow-300 dark:border-yellow-700">

                            <option value="reserved" selected>Reserved</option>

                            <option value="sold" >Sold</option>

                        </select>

                    </td>



                    <!-- Order Status -->

                    <td class="w-36 px-4 py-3">

                        <select onchange="updateOrderStatus(57, this.value)"

                                class="w-full text-xs px-2 py-1 rounded border

                                bg-yellow-50 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-200 border-yellow-300 dark:border-yellow-700">

                            <option value="pending" selected>Pending</option>

                            <option value="payment_received" >Payment Received</option>

                            <option value="processing" >Processing</option>

                            <option value="preparing" >Preparing</option>

                            <option value="ready" >Ready to Ship</option>

                            <option value="in_transit" >In Transit</option>

                            <option value="delivered" >Delivered</option>

                            <option value="completed" >Completed</option>

                            <option value="cancelled" >Cancelled</option>

                            <option value="refunded" >Refunded</option>

                        </select>

                    </td>



                    <!-- Tracking -->

                    <td class="w-32 px-4 py-3">

                        
                            <span class="text-xs text-gray-400 dark:text-gray-500">-</span>

                        
                    </td>



                    <!-- Date -->

                    <td class="w-24 px-4 py-3">

                        <div class="text-xs text-gray-900 dark:text-white">

                            Nov 27
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">

                            09:18 AM
                        </div>

                    </td>



                    <!-- Actions -->

                    <td class="w-36 px-4 py-3">

                        <div class="flex items-center justify-center space-x-1">

                            
                            <button onclick="viewOrderDetails(57)"

                                    class="p-1 text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 hover:bg-blue-50 dark:hover:bg-gray-700 rounded" title="View Details">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>

                                </svg>

                            </button>

                            <button onclick="editNotes(57, '')"

                                    class="p-1 text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 rounded" title="Add Notes">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path>

                                </svg>

                            </button>

                            <button onclick="deleteOrder(57)"

                                    class="p-1 text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300 hover:bg-red-50 dark:hover:bg-gray-700 rounded" title="Delete">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>

                                </svg>

                            </button>

                        </div>

                    </td>

                </tr>

                
                <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 align-middle">

                    <!-- Checkbox -->

                    <td class="w-10 px-2 py-3 text-center">

                        <input type="checkbox" class="order-checkbox rounded border-gray-300 dark:border-gray-600" value="56" onchange="checkSelectedOrders()">

                    </td>



                    <!-- Order -->

                    <td class="w-32 px-4 py-3">

                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                            APL-20251127-0369BF
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">ID: 56</div>

                    </td>



                    <!-- Customer -->

                    <td class="w-40 px-4 py-3">

                        <div class="text-xs">

                            <div class="font-medium text-gray-900 dark:text-white truncate"> </div>

                            <div class="text-gray-500 dark:text-gray-400 truncate">bettywt13@gmail.com</div>

                        </div>

                    </td>



                    <!-- Vehicle -->

                    <td class="w-48 px-4 py-3">

                        <div class="flex items-center">

                            
                                <img src="https://i.imgur.com/QskCOHy.jpeg"

                                     alt="Vehicle"

                                     class="w-12 h-9 object-cover rounded mr-2 flex-shrink-0"

                                     onerror="this.style.display='none'">

                            
                            <div class="min-w-0">

                                <div class="text-xs font-medium text-gray-900 dark:text-white truncate">

                                    2008 Jaguar S-Type 3.0
                                </div>

                                <div class="text-xs text-gray-500 dark:text-gray-400">VIN: 000000</div>

                            </div>

                        </div>

                    </td>



                    <!-- Amount -->

                    <td class="w-24 px-4 py-3">

                        <div class="text-xs font-semibold text-gray-900 dark:text-white">

                            $1,000
                        </div>

                        
                    </td>



                    <!-- Vehicle Status -->

                    <td class="w-32 px-4 py-3">

                        <select onchange="updateVehicleStatus(56, this.value)"

                                class="w-full text-xs px-2 py-1 rounded border

                                bg-yellow-50 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-200 border-yellow-300 dark:border-yellow-700">

                            <option value="reserved" selected>Reserved</option>

                            <option value="sold" >Sold</option>

                        </select>

                    </td>



                    <!-- Order Status -->

                    <td class="w-36 px-4 py-3">

                        <select onchange="updateOrderStatus(56, this.value)"

                                class="w-full text-xs px-2 py-1 rounded border

                                bg-yellow-50 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-200 border-yellow-300 dark:border-yellow-700">

                            <option value="pending" selected>Pending</option>

                            <option value="payment_received" >Payment Received</option>

                            <option value="processing" >Processing</option>

                            <option value="preparing" >Preparing</option>

                            <option value="ready" >Ready to Ship</option>

                            <option value="in_transit" >In Transit</option>

                            <option value="delivered" >Delivered</option>

                            <option value="completed" >Completed</option>

                            <option value="cancelled" >Cancelled</option>

                            <option value="refunded" >Refunded</option>

                        </select>

                    </td>



                    <!-- Tracking -->

                    <td class="w-32 px-4 py-3">

                        
                            <span class="text-xs text-gray-400 dark:text-gray-500">-</span>

                        
                    </td>



                    <!-- Date -->

                    <td class="w-24 px-4 py-3">

                        <div class="text-xs text-gray-900 dark:text-white">

                            Nov 27
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">

                            05:40 AM
                        </div>

                    </td>



                    <!-- Actions -->

                    <td class="w-36 px-4 py-3">

                        <div class="flex items-center justify-center space-x-1">

                            
                            <button onclick="viewOrderDetails(56)"

                                    class="p-1 text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 hover:bg-blue-50 dark:hover:bg-gray-700 rounded" title="View Details">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>

                                </svg>

                            </button>

                            <button onclick="editNotes(56, '')"

                                    class="p-1 text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 rounded" title="Add Notes">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path>

                                </svg>

                            </button>

                            <button onclick="deleteOrder(56)"

                                    class="p-1 text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300 hover:bg-red-50 dark:hover:bg-gray-700 rounded" title="Delete">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>

                                </svg>

                            </button>

                        </div>

                    </td>

                </tr>

                
                <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 align-middle">

                    <!-- Checkbox -->

                    <td class="w-10 px-2 py-3 text-center">

                        <input type="checkbox" class="order-checkbox rounded border-gray-300 dark:border-gray-600" value="54" onchange="checkSelectedOrders()">

                    </td>



                    <!-- Order -->

                    <td class="w-32 px-4 py-3">

                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                            APL-20251121-D5E808
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">ID: 54</div>

                    </td>



                    <!-- Customer -->

                    <td class="w-40 px-4 py-3">

                        <div class="text-xs">

                            <div class="font-medium text-gray-900 dark:text-white truncate"> </div>

                            <div class="text-gray-500 dark:text-gray-400 truncate">robertgerstman7@gmail.com</div>

                        </div>

                    </td>



                    <!-- Vehicle -->

                    <td class="w-48 px-4 py-3">

                        <div class="flex items-center">

                            
                                <img src="https://i.imgur.com/nupgOuI.jpeg"

                                     alt="Vehicle"

                                     class="w-12 h-9 object-cover rounded mr-2 flex-shrink-0"

                                     onerror="this.style.display='none'">

                            
                            <div class="min-w-0">

                                <div class="text-xs font-medium text-gray-900 dark:text-white truncate">

                                    2003 Ford E-450 Class C Sunseeker 24ft
                                </div>

                                <div class="text-xs text-gray-500 dark:text-gray-400">VIN: 00</div>

                            </div>

                        </div>

                    </td>



                    <!-- Amount -->

                    <td class="w-24 px-4 py-3">

                        <div class="text-xs font-semibold text-gray-900 dark:text-white">

                            $1,500
                        </div>

                        
                    </td>



                    <!-- Vehicle Status -->

                    <td class="w-32 px-4 py-3">

                        <select onchange="updateVehicleStatus(54, this.value)"

                                class="w-full text-xs px-2 py-1 rounded border

                                bg-yellow-50 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-200 border-yellow-300 dark:border-yellow-700">

                            <option value="reserved" selected>Reserved</option>

                            <option value="sold" >Sold</option>

                        </select>

                    </td>



                    <!-- Order Status -->

                    <td class="w-36 px-4 py-3">

                        <select onchange="updateOrderStatus(54, this.value)"

                                class="w-full text-xs px-2 py-1 rounded border

                                bg-yellow-50 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-200 border-yellow-300 dark:border-yellow-700">

                            <option value="pending" selected>Pending</option>

                            <option value="payment_received" >Payment Received</option>

                            <option value="processing" >Processing</option>

                            <option value="preparing" >Preparing</option>

                            <option value="ready" >Ready to Ship</option>

                            <option value="in_transit" >In Transit</option>

                            <option value="delivered" >Delivered</option>

                            <option value="completed" >Completed</option>

                            <option value="cancelled" >Cancelled</option>

                            <option value="refunded" >Refunded</option>

                        </select>

                    </td>



                    <!-- Tracking -->

                    <td class="w-32 px-4 py-3">

                        
                            <span class="text-xs text-gray-400 dark:text-gray-500">-</span>

                        
                    </td>



                    <!-- Date -->

                    <td class="w-24 px-4 py-3">

                        <div class="text-xs text-gray-900 dark:text-white">

                            Nov 21
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">

                            04:28 PM
                        </div>

                    </td>



                    <!-- Actions -->

                    <td class="w-36 px-4 py-3">

                        <div class="flex items-center justify-center space-x-1">

                            
                            <button onclick="viewOrderDetails(54)"

                                    class="p-1 text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 hover:bg-blue-50 dark:hover:bg-gray-700 rounded" title="View Details">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>

                                </svg>

                            </button>

                            <button onclick="editNotes(54, '')"

                                    class="p-1 text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 rounded" title="Add Notes">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path>

                                </svg>

                            </button>

                            <button onclick="deleteOrder(54)"

                                    class="p-1 text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300 hover:bg-red-50 dark:hover:bg-gray-700 rounded" title="Delete">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>

                                </svg>

                            </button>

                        </div>

                    </td>

                </tr>

                
                <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 align-middle">

                    <!-- Checkbox -->

                    <td class="w-10 px-2 py-3 text-center">

                        <input type="checkbox" class="order-checkbox rounded border-gray-300 dark:border-gray-600" value="53" onchange="checkSelectedOrders()">

                    </td>



                    <!-- Order -->

                    <td class="w-32 px-4 py-3">

                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                            APL-20251121-3B475A
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">ID: 53</div>

                    </td>



                    <!-- Customer -->

                    <td class="w-40 px-4 py-3">

                        <div class="text-xs">

                            <div class="font-medium text-gray-900 dark:text-white truncate"> </div>

                            <div class="text-gray-500 dark:text-gray-400 truncate">robertgerstman7@gmail.com</div>

                        </div>

                    </td>



                    <!-- Vehicle -->

                    <td class="w-48 px-4 py-3">

                        <div class="flex items-center">

                            
                                <img src="https://i.imgur.com/K6HcpmO.jpeg"

                                     alt="Vehicle"

                                     class="w-12 h-9 object-cover rounded mr-2 flex-shrink-0"

                                     onerror="this.style.display='none'">

                            
                            <div class="min-w-0">

                                <div class="text-xs font-medium text-gray-900 dark:text-white truncate">

                                    1996 Dodge Roadtrek 190 Popular
                                </div>

                                <div class="text-xs text-gray-500 dark:text-gray-400">VIN: 154553</div>

                            </div>

                        </div>

                    </td>



                    <!-- Amount -->

                    <td class="w-24 px-4 py-3">

                        <div class="text-xs font-semibold text-gray-900 dark:text-white">

                            $1,000
                        </div>

                        
                    </td>



                    <!-- Vehicle Status -->

                    <td class="w-32 px-4 py-3">

                        <select onchange="updateVehicleStatus(53, this.value)"

                                class="w-full text-xs px-2 py-1 rounded border

                                bg-yellow-50 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-200 border-yellow-300 dark:border-yellow-700">

                            <option value="reserved" selected>Reserved</option>

                            <option value="sold" >Sold</option>

                        </select>

                    </td>



                    <!-- Order Status -->

                    <td class="w-36 px-4 py-3">

                        <select onchange="updateOrderStatus(53, this.value)"

                                class="w-full text-xs px-2 py-1 rounded border

                                bg-yellow-50 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-200 border-yellow-300 dark:border-yellow-700">

                            <option value="pending" selected>Pending</option>

                            <option value="payment_received" >Payment Received</option>

                            <option value="processing" >Processing</option>

                            <option value="preparing" >Preparing</option>

                            <option value="ready" >Ready to Ship</option>

                            <option value="in_transit" >In Transit</option>

                            <option value="delivered" >Delivered</option>

                            <option value="completed" >Completed</option>

                            <option value="cancelled" >Cancelled</option>

                            <option value="refunded" >Refunded</option>

                        </select>

                    </td>



                    <!-- Tracking -->

                    <td class="w-32 px-4 py-3">

                        
                            <span class="text-xs text-gray-400 dark:text-gray-500">-</span>

                        
                    </td>



                    <!-- Date -->

                    <td class="w-24 px-4 py-3">

                        <div class="text-xs text-gray-900 dark:text-white">

                            Nov 21
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">

                            04:25 PM
                        </div>

                    </td>



                    <!-- Actions -->

                    <td class="w-36 px-4 py-3">

                        <div class="flex items-center justify-center space-x-1">

                            
                            <button onclick="viewOrderDetails(53)"

                                    class="p-1 text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 hover:bg-blue-50 dark:hover:bg-gray-700 rounded" title="View Details">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>

                                </svg>

                            </button>

                            <button onclick="editNotes(53, '')"

                                    class="p-1 text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 rounded" title="Add Notes">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path>

                                </svg>

                            </button>

                            <button onclick="deleteOrder(53)"

                                    class="p-1 text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300 hover:bg-red-50 dark:hover:bg-gray-700 rounded" title="Delete">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>

                                </svg>

                            </button>

                        </div>

                    </td>

                </tr>

                
                <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 align-middle">

                    <!-- Checkbox -->

                    <td class="w-10 px-2 py-3 text-center">

                        <input type="checkbox" class="order-checkbox rounded border-gray-300 dark:border-gray-600" value="52" onchange="checkSelectedOrders()">

                    </td>



                    <!-- Order -->

                    <td class="w-32 px-4 py-3">

                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                            APL-20251121-4B7DDC
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">ID: 52</div>

                    </td>



                    <!-- Customer -->

                    <td class="w-40 px-4 py-3">

                        <div class="text-xs">

                            <div class="font-medium text-gray-900 dark:text-white truncate"> </div>

                            <div class="text-gray-500 dark:text-gray-400 truncate">robertgerstman7@gmail.com</div>

                        </div>

                    </td>



                    <!-- Vehicle -->

                    <td class="w-48 px-4 py-3">

                        <div class="flex items-center">

                            
                                <img src="https://i.imgur.com/q5ONdUC.jpeg"

                                     alt="Vehicle"

                                     class="w-12 h-9 object-cover rounded mr-2 flex-shrink-0"

                                     onerror="this.style.display='none'">

                            
                            <div class="min-w-0">

                                <div class="text-xs font-medium text-gray-900 dark:text-white truncate">

                                    1991 Winnebago Warrior
                                </div>

                                <div class="text-xs text-gray-500 dark:text-gray-400">VIN: 023643</div>

                            </div>

                        </div>

                    </td>



                    <!-- Amount -->

                    <td class="w-24 px-4 py-3">

                        <div class="text-xs font-semibold text-gray-900 dark:text-white">

                            $1,500
                        </div>

                        
                    </td>



                    <!-- Vehicle Status -->

                    <td class="w-32 px-4 py-3">

                        <select onchange="updateVehicleStatus(52, this.value)"

                                class="w-full text-xs px-2 py-1 rounded border

                                bg-yellow-50 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-200 border-yellow-300 dark:border-yellow-700">

                            <option value="reserved" selected>Reserved</option>

                            <option value="sold" >Sold</option>

                        </select>

                    </td>



                    <!-- Order Status -->

                    <td class="w-36 px-4 py-3">

                        <select onchange="updateOrderStatus(52, this.value)"

                                class="w-full text-xs px-2 py-1 rounded border

                                bg-yellow-50 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-200 border-yellow-300 dark:border-yellow-700">

                            <option value="pending" selected>Pending</option>

                            <option value="payment_received" >Payment Received</option>

                            <option value="processing" >Processing</option>

                            <option value="preparing" >Preparing</option>

                            <option value="ready" >Ready to Ship</option>

                            <option value="in_transit" >In Transit</option>

                            <option value="delivered" >Delivered</option>

                            <option value="completed" >Completed</option>

                            <option value="cancelled" >Cancelled</option>

                            <option value="refunded" >Refunded</option>

                        </select>

                    </td>



                    <!-- Tracking -->

                    <td class="w-32 px-4 py-3">

                        
                            <span class="text-xs text-gray-400 dark:text-gray-500">-</span>

                        
                    </td>



                    <!-- Date -->

                    <td class="w-24 px-4 py-3">

                        <div class="text-xs text-gray-900 dark:text-white">

                            Nov 21
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">

                            04:21 PM
                        </div>

                    </td>



                    <!-- Actions -->

                    <td class="w-36 px-4 py-3">

                        <div class="flex items-center justify-center space-x-1">

                            
                            <button onclick="viewOrderDetails(52)"

                                    class="p-1 text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 hover:bg-blue-50 dark:hover:bg-gray-700 rounded" title="View Details">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>

                                </svg>

                            </button>

                            <button onclick="editNotes(52, '')"

                                    class="p-1 text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 rounded" title="Add Notes">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path>

                                </svg>

                            </button>

                            <button onclick="deleteOrder(52)"

                                    class="p-1 text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300 hover:bg-red-50 dark:hover:bg-gray-700 rounded" title="Delete">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>

                                </svg>

                            </button>

                        </div>

                    </td>

                </tr>

                
                <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 align-middle">

                    <!-- Checkbox -->

                    <td class="w-10 px-2 py-3 text-center">

                        <input type="checkbox" class="order-checkbox rounded border-gray-300 dark:border-gray-600" value="51" onchange="checkSelectedOrders()">

                    </td>



                    <!-- Order -->

                    <td class="w-32 px-4 py-3">

                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                            APL-20251118-8CB86B
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">ID: 51</div>

                    </td>



                    <!-- Customer -->

                    <td class="w-40 px-4 py-3">

                        <div class="text-xs">

                            <div class="font-medium text-gray-900 dark:text-white truncate"> </div>

                            <div class="text-gray-500 dark:text-gray-400 truncate">daultonjuanita@gmail.com</div>

                        </div>

                    </td>



                    <!-- Vehicle -->

                    <td class="w-48 px-4 py-3">

                        <div class="flex items-center">

                            
                                <img src="https://i.imgur.com/b9UP3bj.jpeg"

                                     alt="Vehicle"

                                     class="w-12 h-9 object-cover rounded mr-2 flex-shrink-0"

                                     onerror="this.style.display='none'">

                            
                            <div class="min-w-0">

                                <div class="text-xs font-medium text-gray-900 dark:text-white truncate">

                                    2006 Honda Accord LX
                                </div>

                                <div class="text-xs text-gray-500 dark:text-gray-400">VIN: 00000</div>

                            </div>

                        </div>

                    </td>



                    <!-- Amount -->

                    <td class="w-24 px-4 py-3">

                        <div class="text-xs font-semibold text-gray-900 dark:text-white">

                            $800
                        </div>

                        
                    </td>



                    <!-- Vehicle Status -->

                    <td class="w-32 px-4 py-3">

                        <select onchange="updateVehicleStatus(51, this.value)"

                                class="w-full text-xs px-2 py-1 rounded border

                                bg-yellow-50 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-200 border-yellow-300 dark:border-yellow-700">

                            <option value="reserved" selected>Reserved</option>

                            <option value="sold" >Sold</option>

                        </select>

                    </td>



                    <!-- Order Status -->

                    <td class="w-36 px-4 py-3">

                        <select onchange="updateOrderStatus(51, this.value)"

                                class="w-full text-xs px-2 py-1 rounded border

                                bg-yellow-50 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-200 border-yellow-300 dark:border-yellow-700">

                            <option value="pending" selected>Pending</option>

                            <option value="payment_received" >Payment Received</option>

                            <option value="processing" >Processing</option>

                            <option value="preparing" >Preparing</option>

                            <option value="ready" >Ready to Ship</option>

                            <option value="in_transit" >In Transit</option>

                            <option value="delivered" >Delivered</option>

                            <option value="completed" >Completed</option>

                            <option value="cancelled" >Cancelled</option>

                            <option value="refunded" >Refunded</option>

                        </select>

                    </td>



                    <!-- Tracking -->

                    <td class="w-32 px-4 py-3">

                        
                            <span class="text-xs text-gray-400 dark:text-gray-500">-</span>

                        
                    </td>



                    <!-- Date -->

                    <td class="w-24 px-4 py-3">

                        <div class="text-xs text-gray-900 dark:text-white">

                            Nov 18
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">

                            11:04 AM
                        </div>

                    </td>



                    <!-- Actions -->

                    <td class="w-36 px-4 py-3">

                        <div class="flex items-center justify-center space-x-1">

                            
                            <button onclick="viewOrderDetails(51)"

                                    class="p-1 text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 hover:bg-blue-50 dark:hover:bg-gray-700 rounded" title="View Details">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>

                                </svg>

                            </button>

                            <button onclick="editNotes(51, '')"

                                    class="p-1 text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 rounded" title="Add Notes">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path>

                                </svg>

                            </button>

                            <button onclick="deleteOrder(51)"

                                    class="p-1 text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300 hover:bg-red-50 dark:hover:bg-gray-700 rounded" title="Delete">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>

                                </svg>

                            </button>

                        </div>

                    </td>

                </tr>

                
                <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 align-middle">

                    <!-- Checkbox -->

                    <td class="w-10 px-2 py-3 text-center">

                        <input type="checkbox" class="order-checkbox rounded border-gray-300 dark:border-gray-600" value="50" onchange="checkSelectedOrders()">

                    </td>



                    <!-- Order -->

                    <td class="w-32 px-4 py-3">

                        <div class="text-xs font-medium text-gray-900 dark:text-white">

                            APL-20251114-58DB75
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">ID: 50</div>

                    </td>



                    <!-- Customer -->

                    <td class="w-40 px-4 py-3">

                        <div class="text-xs">

                            <div class="font-medium text-gray-900 dark:text-white truncate"> </div>

                            <div class="text-gray-500 dark:text-gray-400 truncate">lflynch@centurylink.net</div>

                        </div>

                    </td>



                    <!-- Vehicle -->

                    <td class="w-48 px-4 py-3">

                        <div class="flex items-center">

                            
                                <img src="https://i.imgur.com/nupgOuI.jpeg"

                                     alt="Vehicle"

                                     class="w-12 h-9 object-cover rounded mr-2 flex-shrink-0"

                                     onerror="this.style.display='none'">

                            
                            <div class="min-w-0">

                                <div class="text-xs font-medium text-gray-900 dark:text-white truncate">

                                    2003 Ford E-450 Class C Sunseeker 24ft
                                </div>

                                <div class="text-xs text-gray-500 dark:text-gray-400">VIN: 00</div>

                            </div>

                        </div>

                    </td>



                    <!-- Amount -->

                    <td class="w-24 px-4 py-3">

                        <div class="text-xs font-semibold text-gray-900 dark:text-white">

                            $1,500
                        </div>

                        
                    </td>



                    <!-- Vehicle Status -->

                    <td class="w-32 px-4 py-3">

                        <select onchange="updateVehicleStatus(50, this.value)"

                                class="w-full text-xs px-2 py-1 rounded border

                                bg-yellow-50 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-200 border-yellow-300 dark:border-yellow-700">

                            <option value="reserved" selected>Reserved</option>

                            <option value="sold" >Sold</option>

                        </select>

                    </td>



                    <!-- Order Status -->

                    <td class="w-36 px-4 py-3">

                        <select onchange="updateOrderStatus(50, this.value)"

                                class="w-full text-xs px-2 py-1 rounded border

                                bg-blue-50 dark:bg-blue-900 text-blue-700 dark:text-blue-200 border-blue-300 dark:border-blue-700">

                            <option value="pending" >Pending</option>

                            <option value="payment_received" selected>Payment Received</option>

                            <option value="processing" >Processing</option>

                            <option value="preparing" >Preparing</option>

                            <option value="ready" >Ready to Ship</option>

                            <option value="in_transit" >In Transit</option>

                            <option value="delivered" >Delivered</option>

                            <option value="completed" >Completed</option>

                            <option value="cancelled" >Cancelled</option>

                            <option value="refunded" >Refunded</option>

                        </select>

                    </td>



                    <!-- Tracking -->

                    <td class="w-32 px-4 py-3">

                        
                            <span class="text-xs text-gray-400 dark:text-gray-500">-</span>

                        
                    </td>



                    <!-- Date -->

                    <td class="w-24 px-4 py-3">

                        <div class="text-xs text-gray-900 dark:text-white">

                            Nov 13
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">

                            11:32 PM
                        </div>

                    </td>



                    <!-- Actions -->

                    <td class="w-36 px-4 py-3">

                        <div class="flex items-center justify-center space-x-1">

                            
                            <button onclick="viewOrderDetails(50)"

                                    class="p-1 text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 hover:bg-blue-50 dark:hover:bg-gray-700 rounded" title="View Details">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>

                                </svg>

                            </button>

                            <button onclick="editNotes(50, '')"

                                    class="p-1 text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 rounded" title="Add Notes">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path>

                                </svg>

                            </button>

                            <button onclick="deleteOrder(50)"

                                    class="p-1 text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300 hover:bg-red-50 dark:hover:bg-gray-700 rounded" title="Delete">

                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>

                                </svg>

                            </button>

                        </div>

                    </td>

                </tr>

                
            </tbody>

        </table>

        
    </div>

</div>



<!-- Order Details Modal -->

<div id="orderDetailsModal" class="hidden fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">

    <div class="bg-white dark:bg-gray-800 rounded-lg max-w-4xl w-full max-h-[90vh] overflow-y-auto">

        <div class="px-6 py-4 border-b dark:border-gray-700 flex justify-between items-center sticky top-0 bg-white dark:bg-gray-800">

            <h2 class="text-lg font-bold text-gray-900 dark:text-white">Order Details</h2>

            <button onclick="closeOrderDetails()" class="text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300">

                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>

                </svg>

            </button>

        </div>

        <div id="orderDetailsContent" class="p-6">

            <!-- Content will be loaded here -->

        </div>

    </div>

</div>



<!-- Add Tracking Modal -->

<div id="trackingModal" class="hidden fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">

    <div class="bg-white dark:bg-gray-800 rounded-lg max-w-md w-full">

        <div class="px-6 py-4 border-b border-gray-200 dark:border-gray-700 flex justify-between items-center">

            <h2 class="text-lg font-bold text-gray-900 dark:text-white">Add Tracking Information</h2>

            <button onclick="closeTrackingModal()" class="text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300">

                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>

                </svg>

            </button>

        </div>

        <form id="trackingForm" class="p-6">

            <input type="hidden" id="trackingOrderId" name="order_id">



            <div class="mb-4">

                <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Tracking Number</label>

                <input type="text" name="tracking_number" required

                       class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

            </div>



            <div class="mb-4">

                <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Carrier</label>

                <select name="carrier" class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                    <option value="">Select Carrier</option>

                    <option value="UPS">UPS</option>

                    <option value="FedEx">FedEx</option>

                    <option value="USPS">USPS</option>

                    <option value="DHL">DHL</option>

                    <option value="Other">Other</option>

                </select>

            </div>



            <div class="flex justify-end gap-3">

                <button type="button" onclick="closeTrackingModal()"

                        class="px-4 py-2 border border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-800 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700">

                    Cancel

                </button>

                <button type="submit" class="px-4 py-2 bg-orange-500 text-white rounded-lg hover:bg-orange-600">

                    Save

                </button>

            </div>

        </form>

    </div>

</div>



<script>

function updateOrderStatus(orderId, status) {
    console.log('Updating order status:', orderId, status);

    // Use FormData (server cannot read JSON!)
    const formData = new FormData();
    formData.append('order_id', orderId);
    formData.append('status', status);

    fetch('/api/admin/update-order-status', {
        method: 'POST',
        credentials: 'same-origin',
        body: formData
    })
    .then(response => {
        console.log('Response status:', response.status);
        return response.json();
    })
    .then(data => {
        console.log('Response data:', data);
        if (data.success) {
            showToast('Order status updated successfully', 'success');
            setTimeout(() => location.reload(), 1000);
        } else {
            showToast(data.message || 'Error updating order status', 'error');

        }

    });

}



function viewOrderDetails(orderId) {

    // Show loading

    document.getElementById('orderDetailsContent').innerHTML = '<div class="text-center py-8"><div class="spinner-border text-gray-400"></div><p class="mt-2 text-gray-500">Loading order details...</p></div>';

    document.getElementById('orderDetailsModal').classList.remove('hidden');



    // Fetch order details

    fetch(`../api/admin/get-order-details.php?order_id=${orderId}`)

        .then(response => response.json())

        .then(data => {

            if (data.success) {

                const order = data.order;

                const html = `

                    <div class="grid grid-cols-2 gap-6">

                        <!-- Order Info -->

                        <div>

                            <h3 class="font-semibold text-gray-900 dark:text-white mb-3">Order Information</h3>

                            <div class="space-y-2 text-sm">

                                <div class="flex justify-between">

                                    <span class="text-gray-600 dark:text-gray-400">Order Number:</span>

                                    <span class="font-medium">${order.order_number}</span>

                                </div>

                                <div class="flex justify-between">

                                    <span class="text-gray-600 dark:text-gray-400">Date:</span>

                                    <span class="font-medium">${new Date(order.created_at).toLocaleDateString()}</span>

                                </div>

                                <div class="flex justify-between">

                                    <span class="text-gray-600 dark:text-gray-400">Status:</span>

                                    <span class="font-medium">${order.status}</span>

                                </div>

                                <div class="flex justify-between">

                                    <span class="text-gray-600 dark:text-gray-400">Vehicle Status:</span>

                                    <span class="font-medium">${order.vehicle_status}</span>

                                </div>

                            </div>

                        </div>



                        <!-- Customer Info -->

                        <div>

                            <h3 class="font-semibold text-gray-900 dark:text-white mb-3">Customer Information</h3>

                            <div class="space-y-2 text-sm">

                                <div class="flex justify-between">

                                    <span class="text-gray-600 dark:text-gray-400">Name:</span>

                                    <span class="font-medium">${order.customer_name || 'N/A'}</span>

                                </div>

                                <div class="flex justify-between">

                                    <span class="text-gray-600 dark:text-gray-400">Email:</span>

                                    <span class="font-medium">${order.customer_email || 'N/A'}</span>

                                </div>

                                <div class="flex justify-between">

                                    <span class="text-gray-600 dark:text-gray-400">Phone:</span>

                                    <span class="font-medium">${order.customer_phone || 'N/A'}</span>

                                </div>

                            </div>

                        </div>



                        <!-- Vehicle Info -->

                        <div>

                            <h3 class="font-semibold text-gray-900 dark:text-white mb-3">Vehicle Information</h3>

                            <div class="space-y-2 text-sm">

                                <div class="flex justify-between">

                                    <span class="text-gray-600 dark:text-gray-400">Vehicle:</span>

                                    <span class="font-medium">${order.vehicle_name || 'N/A'}</span>

                                </div>

                                <div class="flex justify-between">

                                    <span class="text-gray-600 dark:text-gray-400">VIN:</span>

                                    <span class="font-medium">${order.vehicle_vin || 'N/A'}</span>

                                </div>

                                <div class="flex justify-between">

                                    <span class="text-gray-600 dark:text-gray-400">Price:</span>

                                    <span class="font-medium">$${parseFloat(order.vehicle_price || 0).toFixed(2)}</span>

                                </div>

                            </div>

                        </div>



                        <!-- Payment Info -->

                        <div>

                            <h3 class="font-semibold text-gray-900 dark:text-white mb-3">Payment Information</h3>

                            <div class="space-y-2 text-sm">

                                <div class="flex justify-between">

                                    <span class="text-gray-600 dark:text-gray-400">Method:</span>

                                    <span class="font-medium">${order.payment_method || 'N/A'}</span>

                                </div>

                                <div class="flex justify-between">

                                    <span class="text-gray-600 dark:text-gray-400">Total:</span>

                                    <span class="font-medium">$${parseFloat(order.total_amount || 0).toFixed(2)}</span>

                                </div>

                                <div class="flex justify-between">

                                    <span class="text-gray-600 dark:text-gray-400">Status:</span>

                                    <span class="font-medium">${order.payment_status || 'pending'}</span>

                                </div>

                            </div>

                        </div>

                    </div>



                    <!-- Shipping Address -->

                    ${order.shipping_address ? `

                        <div class="mt-6">

                            <h3 class="font-semibold text-gray-900 dark:text-white mb-3">Shipping Address</h3>

                            <div class="text-sm text-gray-600 dark:text-gray-400">

                                ${order.shipping_address}<br>

                                ${order.shipping_city}, ${order.shipping_state} ${order.shipping_zip}

                            </div>

                        </div>

                    ` : ''}



                    <!-- Notes -->

                    ${order.notes ? `

                        <div class="mt-6">

                            <h3 class="font-semibold text-gray-900 dark:text-white mb-3">Notes</h3>

                            <div class="text-sm text-gray-600 dark:text-gray-400 bg-gray-50 dark:bg-gray-900 p-3 rounded">

                                ${order.notes}

                            </div>

                        </div>

                    ` : ''}

                `;

                document.getElementById('orderDetailsContent').innerHTML = html;

            } else {

                document.getElementById('orderDetailsContent').innerHTML = '<div class="text-center text-red-600 dark:text-red-400">Error loading order details</div>';

            }

        })

        .catch(error => {

            console.error('Error:', error);

            document.getElementById('orderDetailsContent').innerHTML = '<div class="text-center text-red-600">Error loading order details</div>';

        });

}



function closeOrderDetails() {

    document.getElementById('orderDetailsModal').classList.add('hidden');

}



function editNotes(orderId, currentNotes) {

    const newNotes = prompt('Edit notes for this order:', currentNotes || '');

    if (newNotes !== null && newNotes !== currentNotes) {

        fetch('/api/admin/update-order-notes.php', {

            method: 'POST',

            headers: {'Content-Type': 'application/json'},

            body: JSON.stringify({order_id: orderId, notes: newNotes})

        })

        .then(response => response.json())

        .then(data => {

            if (data.success) {

                showToast('Notes updated successfully', 'success');

                setTimeout(() => location.reload(), 1000);

            } else {

                showToast('Error updating notes', 'error');

            }

        });

    }

}



function sendEmail(orderId) {

    if (confirm('Send order confirmation email to customer?')) {

        fetch('/api/admin/send-order-email.php', {

            method: 'POST',

            headers: {'Content-Type': 'application/json'},

            body: JSON.stringify({order_id: orderId})

        })

        .then(response => response.json())

        .then(data => {

            if (data.success) {

                showToast('Email sent successfully', 'success');

            } else {

                showToast(data.message || 'Error sending email', 'error');

            }

        });

    }

}



function cancelOrder(orderId) {

    if (confirm('Are you sure you want to cancel this order?')) {

        updateOrderStatus(orderId, 'cancelled');

    }

}



// Function to mark order as read
function markOrderAsRead(orderId) {
    console.log('Marking order as read:', orderId);

    // Use FormData (server cannot read JSON!)
    const formData = new FormData();
    formData.append('order_id', orderId);

    fetch('/api/admin/mark-order-read', {
        method: 'POST',
        credentials: 'same-origin',
        body: formData
    })
    .then(response => {
        console.log('Response status:', response.status);
        return response.json();
    })
    .then(data => {
        console.log('Response data:', data);
        if (data.success) {
            showToast('Order marked as read', 'success');
            // Remove the mark as read button
            setTimeout(() => location.reload(), 500);
        } else {
            showToast(data.message || 'Error marking order as read', 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showToast('Network error', 'error');
    });
}

// New function for updating vehicle status
function updateVehicleStatus(orderId, status) {
    console.log('Updating vehicle status:', orderId, status);

    // Use FormData (server cannot read JSON!)
    const formData = new FormData();
    formData.append('order_id', orderId);
    formData.append('vehicle_status', status);

    fetch('/api/admin/update-vehicle-status', {
        method: 'POST',
        credentials: 'same-origin',
        body: formData
    })
    .then(response => {
        console.log('Response status:', response.status);
        return response.json();
    })
    .then(data => {
        console.log('Response data:', data);
        if (data.success) {
            showToast('Vehicle status updated successfully', 'success');
            // Don't reload page for vehicle status update
        } else {
            showToast(data.message || 'Error updating vehicle status', 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showToast('Network error updating vehicle status', 'error');
    });
}



// Delete single order

function deleteOrder(orderId) {

    if (confirm('Are you sure you want to delete this order? This will also remove it from user purchases and cannot be undone!')) {

        fetch('/api/admin/delete-orders.php?ids=' + orderId, {
            method: 'GET',
            credentials: 'same-origin'
        })

        .then(response => response.json())

        .then(data => {

            if (data.success) {

                showToast('Order deleted successfully', 'success');

                setTimeout(() => location.reload(), 1000);

            } else {

                showToast(data.message || 'Error deleting order', 'error');

            }

        });

    }

}



// Delete selected orders

function deleteSelectedOrders() {

    const checkboxes = document.querySelectorAll('.order-checkbox:checked');

    if (checkboxes.length === 0) {

        showToast('Please select at least one order', 'warning');

        return;

    }



    const orderIds = Array.from(checkboxes).map(cb => cb.value);

    const count = orderIds.length;



    if (confirm(`Are you sure you want to delete ${count} order(s)? This will also remove them from user purchases and cannot be undone!`)) {

        fetch('/api/admin/delete-orders.php?ids=' + orderIds.join(','), {
            method: 'GET',
            credentials: 'same-origin'
        })

        .then(response => response.json())

        .then(data => {

            if (data.success) {

                showToast(`${count} order(s) deleted successfully`, 'success');

                setTimeout(() => location.reload(), 1000);

            } else {

                showToast(data.message || 'Error deleting orders', 'error');

            }

        });

    }

}



// Toggle select all checkboxes

function toggleSelectAll() {

    const selectAll = document.getElementById('selectAll');

    const checkboxes = document.querySelectorAll('.order-checkbox');

    checkboxes.forEach(cb => cb.checked = selectAll.checked);

    checkSelectedOrders();

}



// Check selected orders and enable/disable delete button

function checkSelectedOrders() {

    const checkboxes = document.querySelectorAll('.order-checkbox:checked');

    const deleteBtn = document.getElementById('deleteSelectedBtn');

    deleteBtn.disabled = checkboxes.length === 0;

}



function addTracking(orderId) {

    document.getElementById('trackingOrderId').value = orderId;

    document.getElementById('trackingModal').classList.remove('hidden');

}



function closeTrackingModal() {

    document.getElementById('trackingModal').classList.add('hidden');

    document.getElementById('trackingForm').reset();

}



document.getElementById('trackingForm').addEventListener('submit', function(e) {

    e.preventDefault();

    const formData = new FormData(e.target);



    fetch('/api/admin/update-tracking.php', {

        method: 'POST',

        body: formData

    })

    .then(response => response.json())

    .then(data => {

        if (data.success) {

            showToast('Tracking information added', 'success');

            closeTrackingModal();

            setTimeout(() => location.reload(), 1000);

        } else {

            showToast(data.message || 'Error adding tracking', 'error');

        }

    });

});



function showToast(message, type = 'info') {

    const toast = document.createElement('div');

    toast.className = `fixed top-4 right-4 px-6 py-3 rounded-lg shadow-lg z-50 ${

        type === 'success' ? 'bg-green-500 text-white' :

        type === 'error' ? 'bg-red-500 text-white' :

        'bg-gray-700 text-white'

    }`;

    toast.textContent = message;

    document.body.appendChild(toast);



    setTimeout(() => {

        toast.remove();

    }, 3000);

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