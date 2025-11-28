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

                <a href="?tab=messages" class="sidebar-item active flex items-center px-4 py-3 hover:bg-gray-800 transition">
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
                        Messages                    </h2>
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
                                    <!-- Messages Tab -->
<div class="mb-4 p-3 bg-gray-100 dark:bg-gray-800 rounded-lg">
    <label class="flex items-center">
        <input type="checkbox" id="selectAllMessages" onclick="toggleSelectAllMessages(this)" class="mr-2">
        <span class="font-medium">Select All Messages</span>
    </label>
</div>




<div class="mb-6">

    <!-- Stats Cards -->

    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">

        <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-4">

            <div class="flex items-center">

                <div class="flex-1">

                    <p class="text-gray-500 dark:text-gray-400 text-sm">Total Messages</p>

                    <p class="text-2xl font-bold text-gray-900 dark:text-gray-100">21</p>

                </div>

                <div class="p-2 bg-blue-500 bg-opacity-10 rounded-lg">

                    <svg class="w-6 h-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>

                    </svg>

                </div>

            </div>

        </div>

        

        <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-4">

            <div class="flex items-center">

                <div class="flex-1">

                    <p class="text-gray-500 dark:text-gray-400 text-sm">Unread</p>

                    <p class="text-2xl font-bold text-orange-600">0</p>

                </div>

                <div class="p-2 bg-orange-500 bg-opacity-10 rounded-lg">

                    <svg class="w-6 h-6 text-orange-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"></path>

                    </svg>

                </div>

            </div>

        </div>

        

        <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-4">

            <div class="flex items-center">

                <div class="flex-1">

                    <p class="text-gray-500 dark:text-gray-400 text-sm">Replied</p>

                    <p class="text-2xl font-bold text-green-600">0</p>

                </div>

                <div class="p-2 bg-green-500 bg-opacity-10 rounded-lg">

                    <svg class="w-6 h-6 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h10a8 8 0 018 8v2M3 10l6 6m-6-6l6-6"></path>

                    </svg>

                </div>

            </div>

        </div>

        

        <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-4">

            <div class="flex items-center">

                <div class="flex-1">

                    <p class="text-gray-500 dark:text-gray-400 text-sm">Today</p>

                    <p class="text-2xl font-bold text-purple-600">0</p>

                </div>

                <div class="p-2 bg-purple-500 bg-opacity-10 rounded-lg">

                    <svg class="w-6 h-6 text-purple-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>

                    </svg>

                </div>

            </div>

        </div>

    </div>



    <!-- Filters -->

    <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-4 mb-6">

        <form method="GET" class="flex flex-wrap gap-4">

            <input type="hidden" name="tab" value="messages">

            

            <!-- Search -->

            <div class="flex-1 min-w-[300px]">

                <input type="text" name="messageSearch" value="" 

                       placeholder="Search messages by subject, content, name or email..." 

                       class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

            </div>

            

            <!-- Status Filter -->

            <select name="messageStatus" onchange="this.form.submit()" 

                    class="px-4 py-2 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500">

                <option value="all">All Messages</option>

                <option value="unread" >Unread</option>

                <option value="read" >Read</option>

                <option value="replied" >Replied</option>

            </select>

            

            <button type="submit" class="px-6 py-2 bg-gray-600 dark:bg-gray-700 text-white rounded-lg hover:bg-gray-700 dark:hover:bg-gray-600 transition-colors">

                Search

            </button>

            

            <!-- Mark All Read Button -->

            
        </form>

    </div>

</div>



<!-- Messages List (Compact View) -->

<div class="bg-white dark:bg-gray-800 rounded-lg shadow overflow-hidden">

    <table class="min-w-full">

        <thead class="bg-gray-50 dark:bg-gray-900 border-b border-gray-200 dark:border-gray-700">

            <tr>

                <th class="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Status</th>

                <th class="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">From</th>

                <th class="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Subject</th>

                <th class="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Message</th>

                <th class="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Date</th>

                <th class="px-3 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Actions</th>

            </tr>

        </thead>

        <tbody class="bg-white dark:bg-gray-800 divide-y divide-gray-200 dark:divide-gray-700">

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            Juanita daulton 
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">daultonjuanita84@gmail.com</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        Honda accord 
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="I&#039;m interested in buying the honda accord for 800.00 and could it be delivered to Knoxville tn ">

                        I&#039;m interested in buying the honda accord for 800.00 and could it be delivered to Knoxville tn 
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 18, 10:27
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(72)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(72)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            Frank Lynch
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">lflynch@centurylink.net</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        invoice APL-20251111-DC319A
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="Gentlemen.  I am inquiring about invoice APL-20251111-DC319A Ford F-450 class-c.

I believe I purchased it on 11/12/25 and was told transportation was being arranged.

Can you give me an update?
L.F. Lynch
1629 S. Pacific st.
Boise Idaho  83705
208 343-6231
">

                        Gentlemen.  I am inquiring about invoice APL-20251111-DC319A Ford F-450 class-c.

I believe I purc...
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 17, 14:22
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(71)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(71)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            Marilynn McClean
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">aboout@airegistry.pro</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        Does ChatGPT know about autorebound.com?
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="More and more people skip Google Search and ask ChatGPT to search for everything.

Add autorebound.com to our AI-optimized directory to help them find autorebound.com

Join now: https://AIREG.pro/">

                        More and more people skip Google Search and ask ChatGPT to search for everything.

Add autorebound...
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 14, 16:48
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(69)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(69)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            L. F. Lynch
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">lflynch@centurylink.net</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        Status of my purchase from you. 
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="Gentleman I have paid for a vehicle from you, but have yet to receive any delivery information or transportation.  Can you please call me back at 208-343-6231 and verify my purchase?">

                        Gentleman I have paid for a vehicle from you, but have yet to receive any delivery information or tr...
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 14, 15:18
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(68)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(68)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            Nikita 
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">nikita@rocketdigitaltech.com</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        Website ranking on google 
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="Hello http://autorebound.com,

I checked your website. You have an impressive site but ranking is not good on Google, Yahoo and Bing.

Would you like to optimize your site?

If you’re interested, then I will send you SEO Packages and strategies.

Can I send?

Warm regards,
Nikita
">

                        Hello http://autorebound.com,

I checked your website. You have an impressive site but ranking is ...
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 14, 14:57
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(67)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(67)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            Matthew Horan
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">matthewhoran0@gmail.com</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        1991 Winnebago Warrior
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="Hey there! I&#039;m new to buying repo vehicles, and I stumbled across your site. I&#039;m interested in your 1991 Winnebago Warrior. I&#039;m located in Philadelphia, PA, so I&#039;m curious as to what shipping looks like as well as the title transfer. If you could include any other information that I may be missing, I&#039;d appreciate it!">

                        Hey there! I&#039;m new to buying repo vehicles, and I stumbled across your site. I&#039;m interested in your ...
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 14, 10:40
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(66)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(66)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            Frank Lynch
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">LFLYNCH@CENTURYLINK.NET</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        need transportation info on purchase.  
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="Gentlemen:
Yesterday I received confirmation of purchase

Re: Invoice APL-20251111-D3C19A 2003 Ford E-450 Class C

&quot;&quot;Mr Frank
Payment has been confirmed. The delivery process will begin in the next few hours...&quot;&quot;

I have heard nothing since.  
can you confirm, shipping??

L. Frank Lynch
1629 s Pacific st. 
Boise, Id. 83705
208 343-6231
lflynch@centurylink.net">

                        Gentlemen:
Yesterday I received confirmation of purchase

Re: Invoice APL-20251111-D3C19A 2003 Fo...
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 13, 23:39
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(65)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(65)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            Frank Lynch
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">LFLYNCH@CENTURYLINK.NET</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        Re: Invoice APL-20251111-D3C19A 2003 Ford E-450 Class C   ...request info
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="
I was wpndering if you can provide further confirmation of this purchase or the transportation data?  I dont see it credited to my account.

Frank Lynch 208 343-6231

I have received this confirmation from your man at 505 456-3272  I believe he said his name was Marvin Hopkins?

Mr Frank

Payment has been confirmed. The delivery process will begin in the next few hours. Keep me updated on the RMN results.
">

                        
I was wpndering if you can provide further confirmation of this purchase or the transportation dat...
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 13, 19:46
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(64)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(64)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            arthur waits
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">sugahbooger22@aol.com</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        rvs 
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="i did no reponce arthur waits">

                        i did no reponce arthur waits
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 13, 12:02
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(62)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(62)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            arthur waits
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">sugahbooger22@aol.com</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        rvs 
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="i did no reponce arthur waits">

                        i did no reponce arthur waits
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 13, 12:01
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(61)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(61)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            arthur waits
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">sugahbooger22@aol.com</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        rvs 
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="i did no reponce arthur waits">

                        i did no reponce arthur waits
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 13, 11:50
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(60)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(60)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            ARTHUR WAITS
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">SUGAHBOOGER22@AOL.COM</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                         1500 RV 2003 FORD 1500 .00
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="2003  FORD RV ">

                        2003  FORD RV 
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 12, 16:34
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(57)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(57)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            Clinton Pare
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">clintonrpare@gmail.com</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        91 toyota winnebago
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="Yes, I&#039;m interested in this RV.  Where are you located so that i can see if?  I said you are located in Hartford Connecticut.   Please use my number to text me.  I have problems with getting my emails where I am at this time.  Thanks   

My sister has been looking for me.  ">

                        Yes, I&#039;m interested in this RV.  Where are you located so that i can see if?  I said you are located...
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 11, 13:50
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(56)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(56)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            Frank Lynch
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">lflynch@centurylink.net</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        Cannot login to pay for purchase
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="Gentlemen,
Last night I created an account an logged in wanting to buy a vehicle, this morning I cannot log back in, and the forgot password feature doesn&#039;t work for me.  Can you help me recover my account so I can buy your products?
">

                        Gentlemen,
Last night I created an account an logged in wanting to buy a vehicle, this morning I ca...
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 11, 11:41
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(55)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(55)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            Frank Lynch
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">lflynch@centurylink.net</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        STK3005 location and availability? 
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="A 2003 Ford sunseeker would be a fabulous addition to my life right now. Would be interested in location and availability.  
Thanks. ">

                        A 2003 Ford sunseeker would be a fabulous addition to my life right now. Would be interested in loca...
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 10, 15:32
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(53)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(53)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            Frank Lynch
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">lflynch@centurylink.net</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        STK3005 location and availability? 
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="A 2003 Ford sunseeker would be a fabulous addition to my life right now. Would be interested in location and availability.  
Thanks. ">

                        A 2003 Ford sunseeker would be a fabulous addition to my life right now. Would be interested in loca...
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 10, 15:32
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(54)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(54)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            Frank Lynch
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">lflynch@centurylink.net</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        STK3005 location and availability? 
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="A 2003 Ford sunseeker would be a fabulous addition to my life right now. Would be interested in location and availability.  
Thanks. ">

                        A 2003 Ford sunseeker would be a fabulous addition to my life right now. Would be interested in loca...
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 10, 15:32
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(52)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(52)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            Robert Gerstman
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">robertgerstman7@gmail.com</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        Rv stk3005
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="You have to tell me how to buy it">

                        You have to tell me how to buy it
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 10, 13:57
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(51)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(51)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            Patricia Costs 
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">patriciaolivierbr@gmail.com</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        Information 
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="I need more information about the RV condition…. ">

                        I need more information about the RV condition…. 
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 07, 10:43
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(50)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(50)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            Marco tulio galindo Sanchez 
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">marcotuliogalindo940@gmail.com</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        Quiero la toyota tacoma
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="Estoy interesado en un vehiculo">

                        Estoy interesado en un vehiculo
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 05, 16:56
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(49)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(49)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
            <tr class="hover:bg-gray-50 dark:hover:bg-gray-700 ">

                <td class="px-3 py-2 whitespace-nowrap">

                    
                        <span class="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 rounded">READ</span>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm">

                        <div class="font-medium text-gray-900 dark:text-white">

                            Stanley Persley 
                        </div>

                        <div class="text-xs text-gray-500 dark:text-gray-400">Persleys965@gmail.com</div>

                    </div>

                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-900 dark:text-white font-medium">

                        1993- $800
                    </div>

                    
                </td>

                <td class="px-3 py-2">

                    <div class="text-sm text-gray-600 dark:text-gray-400 max-w-xs truncate" title="Am Interested in buying the 1993-fleetwood for $800">

                        Am Interested in buying the 1993-fleetwood for $800
                    </div>

                </td>

                <td class="px-3 py-2 whitespace-nowrap text-xs text-gray-500 dark:text-gray-400">

                    Nov 03, 13:59
                </td>

                <td class="px-3 py-2 whitespace-nowrap text-sm">

                    <button onclick="viewMessage(42)" class="text-blue-600 dark:text-blue-400 hover:text-blue-900 dark:hover:text-blue-300 mr-2">View</button>

                    
                    <button onclick="deleteMessage(42)" class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300">Delete</button>

                </td>

            </tr>

            
        </tbody>

    </table>



    
</div>



<!-- Message Detail Modal -->

<div id="messageModal" class="fixed inset-0 bg-black bg-opacity-50 dark:bg-opacity-75 hidden z-50 flex items-center justify-center">

    <div class="bg-white dark:bg-gray-800 rounded-lg max-w-2xl w-full m-4 max-h-[80vh] overflow-y-auto">

        <div class="p-6">

            <div class="flex justify-between items-start mb-4">

                <h3 id="modalSubject" class="text-lg font-semibold text-gray-900 dark:text-white"></h3>

                <button onclick="closeModal()" class="text-gray-400 dark:text-gray-500 hover:text-gray-600 dark:hover:text-gray-300">

                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>

                    </svg>

                </button>

            </div>

            <div id="modalContent"></div>

        </div>

    </div>

</div>





<script>

// Store messages data for modal display

const messagesData = [{"id":"72","subject":"Honda accord ","message":"I'm interested in buying the honda accord for 800.00 and could it be delivered to Knoxville tn ","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-18 10:27:13","sender_name":"Juanita daulton ","sender_email":"daultonjuanita84@gmail.com","sender_phone":"+18653049050","user_id":null,"ip_address":null,"first_name":null,"last_name":null,"user_email":null,"user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"71","subject":"invoice APL-20251111-DC319A","message":"Gentlemen.  I am inquiring about invoice APL-20251111-DC319A Ford F-450 class-c.\r\n\r\nI believe I purchased it on 11\/12\/25 and was told transportation was being arranged.\r\n\r\nCan you give me an update?\r\nL.F. Lynch\r\n1629 S. Pacific st.\r\nBoise Idaho  83705\r\n208 343-6231\r\n","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-17 14:22:12","sender_name":"Frank Lynch","sender_email":"lflynch@centurylink.net","sender_phone":"208 343-6231","user_id":null,"ip_address":null,"first_name":null,"last_name":null,"user_email":null,"user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"69","subject":"Does ChatGPT know about autorebound.com?","message":"More and more people skip Google Search and ask ChatGPT to search for everything.\r\n\r\nAdd autorebound.com to our AI-optimized directory to help them find autorebound.com\r\n\r\nJoin now: https:\/\/AIREG.pro\/","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-14 16:48:46","sender_name":"Marilynn McClean","sender_email":"aboout@airegistry.pro","sender_phone":"9056129505","user_id":null,"ip_address":null,"first_name":null,"last_name":null,"user_email":null,"user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"68","subject":"Status of my purchase from you. ","message":"Gentleman I have paid for a vehicle from you, but have yet to receive any delivery information or transportation.  Can you please call me back at 208-343-6231 and verify my purchase?","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-14 15:18:42","sender_name":"L. F. Lynch","sender_email":"lflynch@centurylink.net","sender_phone":"2083436231","user_id":null,"ip_address":null,"first_name":null,"last_name":null,"user_email":null,"user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"67","subject":"Website ranking on google ","message":"Hello http:\/\/autorebound.com,\r\n\r\nI checked your website. You have an impressive site but ranking is not good on Google, Yahoo and Bing.\r\n\r\nWould you like to optimize your site?\r\n\r\nIf you\u2019re interested, then I will send you SEO Packages and strategies.\r\n\r\nCan I send?\r\n\r\nWarm regards,\r\nNikita\r\n","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-14 14:57:50","sender_name":"Nikita ","sender_email":"nikita@rocketdigitaltech.com","sender_phone":"7532833829","user_id":null,"ip_address":null,"first_name":null,"last_name":null,"user_email":null,"user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"66","subject":"1991 Winnebago Warrior","message":"Hey there! I'm new to buying repo vehicles, and I stumbled across your site. I'm interested in your 1991 Winnebago Warrior. I'm located in Philadelphia, PA, so I'm curious as to what shipping looks like as well as the title transfer. If you could include any other information that I may be missing, I'd appreciate it!","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-14 10:40:37","sender_name":"Matthew Horan","sender_email":"matthewhoran0@gmail.com","sender_phone":"+1 267 566 1398","user_id":null,"ip_address":null,"first_name":null,"last_name":null,"user_email":null,"user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"65","subject":"need transportation info on purchase.  ","message":"Gentlemen:\r\nYesterday I received confirmation of purchase\r\n\r\nRe: Invoice APL-20251111-D3C19A 2003 Ford E-450 Class C\r\n\r\n\"\"Mr Frank\r\nPayment has been confirmed. The delivery process will begin in the next few hours...\"\"\r\n\r\nI have heard nothing since.  \r\ncan you confirm, shipping??\r\n\r\nL. Frank Lynch\r\n1629 s Pacific st. \r\nBoise, Id. 83705\r\n208 343-6231\r\nlflynch@centurylink.net","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-13 23:39:44","sender_name":"Frank Lynch","sender_email":"LFLYNCH@CENTURYLINK.NET","sender_phone":"","user_id":"58","ip_address":null,"first_name":"Frank","last_name":"Lynch","user_email":"LFLYNCH@CENTURYLINK.NET","user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"64","subject":"Re: Invoice APL-20251111-D3C19A 2003 Ford E-450 Class C   ...request info","message":"\r\nI was wpndering if you can provide further confirmation of this purchase or the transportation data?  I dont see it credited to my account.\r\n\r\nFrank Lynch 208 343-6231\r\n\r\nI have received this confirmation from your man at 505 456-3272  I believe he said his name was Marvin Hopkins?\r\n\r\nMr Frank\r\n\r\nPayment has been confirmed. The delivery process will begin in the next few hours. Keep me updated on the RMN results.\r\n","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-13 19:46:51","sender_name":"Frank Lynch","sender_email":"LFLYNCH@CENTURYLINK.NET","sender_phone":"","user_id":"58","ip_address":null,"first_name":"Frank","last_name":"Lynch","user_email":"LFLYNCH@CENTURYLINK.NET","user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"62","subject":"rvs ","message":"i did no reponce arthur waits","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-13 12:02:56","sender_name":"arthur waits","sender_email":"sugahbooger22@aol.com","sender_phone":"803210 5567","user_id":null,"ip_address":null,"first_name":null,"last_name":null,"user_email":null,"user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"61","subject":"rvs ","message":"i did no reponce arthur waits","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-13 12:01:14","sender_name":"arthur waits","sender_email":"sugahbooger22@aol.com","sender_phone":"803210 5567","user_id":null,"ip_address":null,"first_name":null,"last_name":null,"user_email":null,"user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"60","subject":"rvs ","message":"i did no reponce arthur waits","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-13 11:50:38","sender_name":"arthur waits","sender_email":"sugahbooger22@aol.com","sender_phone":"803210 5567","user_id":null,"ip_address":null,"first_name":null,"last_name":null,"user_email":null,"user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"57","subject":" 1500 RV 2003 FORD 1500 .00","message":"2003  FORD RV ","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-12 16:34:57","sender_name":"ARTHUR WAITS","sender_email":"SUGAHBOOGER22@AOL.COM","sender_phone":"8032105567","user_id":null,"ip_address":null,"first_name":null,"last_name":null,"user_email":null,"user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"56","subject":"91 toyota winnebago","message":"Yes, I'm interested in this RV.  Where are you located so that i can see if?  I said you are located in Hartford Connecticut.   Please use my number to text me.  I have problems with getting my emails where I am at this time.  Thanks   \r\n\r\nMy sister has been looking for me.  ","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-11 13:50:46","sender_name":"Clinton Pare","sender_email":"clintonrpare@gmail.com","sender_phone":"860-805-4305","user_id":null,"ip_address":null,"first_name":null,"last_name":null,"user_email":null,"user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"55","subject":"Cannot login to pay for purchase","message":"Gentlemen,\r\nLast night I created an account an logged in wanting to buy a vehicle, this morning I cannot log back in, and the forgot password feature doesn't work for me.  Can you help me recover my account so I can buy your products?\r\n","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-11 11:41:02","sender_name":"Frank Lynch","sender_email":"lflynch@centurylink.net","sender_phone":"2083436231","user_id":null,"ip_address":null,"first_name":null,"last_name":null,"user_email":null,"user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"53","subject":"STK3005 location and availability? ","message":"A 2003 Ford sunseeker would be a fabulous addition to my life right now. Would be interested in location and availability.  \r\nThanks. ","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-10 15:32:14","sender_name":"Frank Lynch","sender_email":"lflynch@centurylink.net","sender_phone":"208 343-6231","user_id":null,"ip_address":null,"first_name":null,"last_name":null,"user_email":null,"user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"54","subject":"STK3005 location and availability? ","message":"A 2003 Ford sunseeker would be a fabulous addition to my life right now. Would be interested in location and availability.  \r\nThanks. ","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-10 15:32:14","sender_name":"Frank Lynch","sender_email":"lflynch@centurylink.net","sender_phone":"208 343-6231","user_id":null,"ip_address":null,"first_name":null,"last_name":null,"user_email":null,"user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"52","subject":"STK3005 location and availability? ","message":"A 2003 Ford sunseeker would be a fabulous addition to my life right now. Would be interested in location and availability.  \r\nThanks. ","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-10 15:32:13","sender_name":"Frank Lynch","sender_email":"lflynch@centurylink.net","sender_phone":"208 343-6231","user_id":null,"ip_address":null,"first_name":null,"last_name":null,"user_email":null,"user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"51","subject":"Rv stk3005","message":"You have to tell me how to buy it","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-10 13:57:00","sender_name":"Robert Gerstman","sender_email":"robertgerstman7@gmail.com","sender_phone":"6313840724","user_id":null,"ip_address":null,"first_name":null,"last_name":null,"user_email":null,"user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"50","subject":"Information ","message":"I need more information about the RV condition\u2026. ","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-07 10:43:47","sender_name":"Patricia Costs ","sender_email":"patriciaolivierbr@gmail.com","sender_phone":"","user_id":"51","ip_address":null,"first_name":"Patricia","last_name":"Costs ","user_email":"patriciaolivierbr@gmail.com","user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"49","subject":"Quiero la toyota tacoma","message":"Estoy interesado en un vehiculo","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-05 16:56:04","sender_name":"Marco tulio galindo Sanchez ","sender_email":"marcotuliogalindo940@gmail.com","sender_phone":"2406045425","user_id":null,"ip_address":null,"first_name":null,"last_name":null,"user_email":null,"user_phone":null,"vehicle_name_ref":null,"vehicle_price":null},{"id":"42","subject":"1993- $800","message":"Am Interested in buying the 1993-fleetwood for $800","vehicle_id":null,"vehicle_name":null,"status":"read","reply":null,"replied_at":null,"replied_by":null,"created_at":"2025-11-03 13:59:17","sender_name":"Stanley Persley ","sender_email":"Persleys965@gmail.com","sender_phone":"2145417557","user_id":null,"ip_address":null,"first_name":null,"last_name":null,"user_email":null,"user_phone":null,"vehicle_name_ref":null,"vehicle_price":null}];



// View message in modal with full user details

function viewMessage(messageId) {

    const message = messagesData.find(m => m.id == messageId);

    if (!message) return;



    const modal = document.getElementById('messageModal');

    document.getElementById('modalSubject').textContent = message.subject || 'No subject';



    // Get user details

    const userName = message.sender_name || (message.first_name ? message.first_name + ' ' + message.last_name : '') || 'Anonymous';

    const userEmail = message.sender_email || message.user_email || 'Not provided';

    const userPhone = message.sender_phone || message.user_phone || 'Not provided';



    let content = `

        <div class="space-y-4">

            <!-- Sender Details Section -->

            <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-4">

                <h4 class="font-semibold text-gray-900 dark:text-white mb-3">Sender Information</h4>

                <div class="grid grid-cols-2 gap-3">

                    <div>

                        <p class="text-xs text-gray-500 dark:text-gray-400 uppercase tracking-wider">Name</p>

                        <p class="text-sm font-medium text-gray-900 dark:text-white">${userName}</p>

                    </div>

                    <div>

                        <p class="text-xs text-gray-500 dark:text-gray-400 uppercase tracking-wider">Email</p>

                        <p class="text-sm font-medium text-gray-900 dark:text-white">${userEmail}</p>

                    </div>

                    <div>

                        <p class="text-xs text-gray-500 dark:text-gray-400 uppercase tracking-wider">Phone</p>

                        <p class="text-sm font-medium text-gray-900 dark:text-white">${userPhone}</p>

                    </div>

                    <div>

                        <p class="text-xs text-gray-500 dark:text-gray-400 uppercase tracking-wider">IP Address</p>

                        <p class="text-sm font-medium text-gray-900 dark:text-white">${message.ip_address || 'Not recorded'}</p>

                    </div>

                    ${message.user_id ? `

                    <div>

                        <p class="text-xs text-gray-500 dark:text-gray-400 uppercase tracking-wider">User ID</p>

                        <p class="text-sm font-medium text-gray-900 dark:text-white">#${message.user_id}</p>

                    </div>

                    ` : ''}

                    <div>

                        <p class="text-xs text-gray-500 dark:text-gray-400 uppercase tracking-wider">Date Sent</p>

                        <p class="text-sm font-medium text-gray-900 dark:text-white">${new Date(message.created_at).toLocaleString()}</p>

                    </div>

                </div>

            </div>



            <!-- Message Content -->

            <div>

                <h4 class="font-semibold text-gray-900 dark:text-white mb-2">Message</h4>

                <div class="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg p-4">

                    <p class="text-gray-700 dark:text-gray-300 whitespace-pre-wrap">${message.message}</p>

                </div>

            </div>

    `;



    if (message.vehicle_name_ref) {

        content += `

            <!-- Vehicle Information -->

            <div class="bg-blue-50 dark:bg-blue-900 rounded-lg p-4">

                <h4 class="font-semibold text-blue-900 dark:text-blue-200 mb-2">Related Vehicle</h4>

                <p class="text-sm text-blue-800 dark:text-blue-300">

                    ${message.vehicle_name_ref}

                    ${message.vehicle_price ? ` - $${parseFloat(message.vehicle_price).toLocaleString()}` : ''}

                    ${message.vehicle_id ? ` (ID: #${message.vehicle_id})` : ''}

                </p>

            </div>

        `;

    }



    content += '</div>';



    document.getElementById('modalContent').innerHTML = content;

    modal.classList.remove('hidden');

}



// Close modal

function closeModal() {

    document.getElementById('messageModal').classList.add('hidden');

}





// Override the global functions for messages specifically
// These functions will use the simple APIs that work

function markMessageAsRead(messageId) {
    fetch('/api/admin/simple-mark-message-read.php?message_id=' + messageId, {
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
        alert('Error: ' + error.message);
    });
}

function markAllMessagesAsRead() {
    if (confirm('Mark all messages as read?')) {
        fetch('/api/admin/simple-mark-all-messages-read.php', {
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
            alert('Error: ' + error.message);
        });
    }
}



// Delete Message

async function deleteMessage(messageId) {
    if (confirm('Are you sure you want to delete this message?')) {
        try {
            const response = await fetch('/api/admin/delete-message.php?message_id=' + messageId, {
                method: 'GET',
                
                credentials: 'same-origin',
                
            });

            const result = await response.json();
            if (result.success) {
                alert('Message deleted');
                location.reload();
            } else {
                alert('Error: ' + result.message);
            }
        } catch (error) {
            alert('Error deleting message');
        }
    }
}


// Bulk delete functions for messages
function toggleSelectAllMessages(source) {
    const checkboxes = document.querySelectorAll('.message-checkbox');
    checkboxes.forEach(checkbox => {
        checkbox.checked = source.checked;
    });
}

function deleteSelectedMessages() {
    const checkboxes = document.querySelectorAll('.message-checkbox:checked');
    const selectedIds = Array.from(checkboxes).map(cb => cb.value);

    if (selectedIds.length === 0) {
        alert('Please select at least one message to delete');
        return;
    }

    if (confirm(`Are you sure you want to delete ${selectedIds.length} message(s)?`)) {
        fetch('/api/admin/delete-messages.php?ids=' + selectedIds.join(','), {
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
            alert('Error deleting messages');
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