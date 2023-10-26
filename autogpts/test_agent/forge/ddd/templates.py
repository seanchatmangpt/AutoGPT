head = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Lorem Ipsum</title>
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body>"""

navigation_bar = """<!-- Navigation Bar -->
  <nav class="fixed top-0 left-0 w-full bg-gray-800 py-4 px-6 flex items-center justify-between">
    <h1 class="text-white text-xl font-bold">Lorem Ipsum</h1>
    <div class="hidden md:block">
      <a href="#home" class="text-gray-300 hover:text-white hover:underline mx-4">Lorem</a>
      <a href="#features" class="text-gray-300 hover:text-white hover:underline mx-4">Lorem</a>
      <a href="#testimonials" class="text-gray-300 hover:text-white hover:underline mx-4">Lorem</a>
      <a href="#contact" class="text-gray-300 hover:text-white hover:underline mx-4">Lorem</a>
    </div>
  </nav>
"""

hero_section = """<!-- Hero Section -->
<section class="bg-gray-100 py-20 px-6">
  <div class="max-w-6xl mx-auto text-center">
    <h2 class="text-4xl sm:text-5xl font-bold mb-4">Lorem ipsum dolor sit amet</h2>
    <p class="text-lg text-gray-700 mb-8">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <a href="#features" class="px-8 py-4 bg-green-500 text-white font-medium rounded hover:bg-green-600">Lorem Ipsum</a>
  </div>
</section>
"""

features_section = """<!-- Features Section -->
<section id="features" class="py-20 px-6 bg-gray-200">
  <h3 class="text-3xl sm:text-4xl font-bold text-center mb-12">Key Features</h3>
  <div class="max-w-6xl mx-auto flex flex-wrap justify-center">
    <div class="w-full sm:w-1/2 lg:w-1/3 px-4 mb-8">
      <div class="bg-white p-6 rounded-lg">
        <div class="flex items-center mb-4">
          <img src="https://img.icons8.com/bubbles/50/000000/coding.png" class="h-12 w-12 mr-4"/>
          <h4 class="text-lg font-bold">Lorem Ipsum</h4>
        </div>
        <p class="text-gray-700">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla euismod nisi vel bibendum viverra.</p>
      </div>
    </div>
    <div class="w-full sm:w-1/2 lg:w-1/3 px-4 mb-8">
      <div class="bg-white p-6 rounded-lg">
        <div class="flex items-center mb-4">
          <img src="https://img.icons8.com/cotton/64/000000/window-network--v1.png" class="h-12 w-12 mr-4"/>
          <h4 class="text-lg font-bold">Lorem Ipsum</h4>
        </div>
        <p class="text-gray-700">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla euismod nisi vel bibendum viverra.</p>
      </div>
    </div>
    <div class="w-full sm:w-1/2 lg:w-1/3 px-4 mb-8">
      <div class="bg-white p-6 rounded-lg">
        <div class="flex items-center mb-4">
          <img src="https://img.icons8.com/window/64/000000/ai-robot--v1.png" class="h-12 w-12 mr-4"/>
          <h4 class="text-lg font-bold">Lorem Ipsum</h4>
        </div>
        <p class="text-gray-700">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla euismod nisi vel bibendum viverra.</p>
      </div>
    </div>
  </div>
</section>
"""

testimonials_section = """<!-- Testimonials Section -->
<section id="testimonials" class="bg-gray-100 py-20 px-6">
  <h3 class="text-3xl sm:text-4xl font-bold text-center mb-12">Lorem Ipsum Testimonials</h3>
  <div class="max-w-6xl mx-auto flex flex-wrap justify-center">
    <div class="w-full sm:w-1/2 lg:w-1/3 px-4 mb-8">
      <div class="bg-white p-6 rounded-lg">
        <div class="flex items-center mb-4">
          <img src="https://randomuser.me/api/portraits/women/44.jpg" class="h-12 w-12 rounded-full mr-4"/>
          <div>
            <h4 class="text-lg font-bold">Lorem Ipsum</h4>
            <p class="text-gray-700">Lorem Ipsum</p>
          </div>
        </div>
        <p class="text-gray-700">"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut nunc nec leo ullamcorper interdum. Pellentesque euismod mi vel eros commodo, eget lacinia metus posuere."</p>
      </div>
    </div>
    <div class="w-full sm:w-1/2 lg:w-1/3 px-4 mb-8">
      <div class="bg-white p-6 rounded-lg">
        <div class="flex items-center mb-4">
          <img src="https://randomuser.me/api/portraits/men/46.jpg" class="h-12 w-12 rounded-full mr-4"/>
          <div>
            <h4 class="text-lg font-bold">Lorem Ipsum</h4>
            <p class="text-gray-700">Lorem Ipsum</p>
          </div>
        </div>
        <p class="text-gray-700">"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut nunc nec leo ullamcorper interdum. Pellentesque euismod mi vel eros commodo, eget lacinia metus posuere."</p>
      </div>
    </div>
    <div class="w-full sm:w-1/2 lg:w-1/3 px-4 mb-8">
      <div class="bg-white p-6 rounded-lg">
        <div class="flex items-center mb-4">
          <img src="https://randomuser.me/api/portraits/women/72.jpg" class="h-12 w-12 rounded-full mr-4"/>
          <div>
            <h4 class="text-lg font-bold">Lorem Ipsum</h4>
            <p class="text-gray-700">Lorem Ipsum</p>
          </div>
        </div>
        <p class="text-gray-700">"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut nunc nec leo ullamcorper interdum. Pellentesque euismod mi vel eros commodo, eget lacinia metus posuere."</p>
      </div>
    </div>
  </div>
</section>"""

footer_section = """  <!-- Footer Section -->
  <footer id="contact" class="bg-gray-800 py-8 px-6">
    <div class="max-w-6xl mx-auto flex flex-wrap justify-between">
      <div class="w-full sm:w-1/2 lg:w-1/4 mb-8">
        <h4 class="text-xl font-bold text-white mb-4">Job Interview AI Agent</h4>
        <p class="text-gray-400 mb-2">123 Main Street</p>
        <p class="text-gray-400 mb-2">New York, NY 10001</p>
        <p class="text-gray-400 mb-2">info@jobinterviewaiagent.com</p>
      </div>
      <div class="w-full sm:w-1/2 lg:w-1/4 mb-8">
        <h4 class="text-xl font-bold text-white mb-4">Follow Us</h4>
        <div class="flex items-center">
          <a href="#" class="text-white mr-4 hover:text-green-500"><img src="https://img.icons8.com/fluency/48/000000/twitter.png" class="h-8 w-8"/></a>
          <a href="#" class="text-white hover:text-green-500"><img src="https://img.icons8.com/color/48/000000/linkedin.png" class="h-8 w-8"/></a>
        </div>
      </div>
      <div class="w-full sm:w-1/2 lg:w-1/4 mb-8">
        <h4 class="text-xl font-bold text-white mb-4">Resources</h4>
        <a href="#" class="text-gray-400 hover:text-white block mb-2">Terms of Service</a>
        <a href="#" class="text-gray-400 hover:text-white block mb-2">Privacy Policy</a>
        <a href="#" class="text-gray-400 hover:text-white block mb-2">Disclaimer</a>
      </div>
    </div>
  </footer>"""
