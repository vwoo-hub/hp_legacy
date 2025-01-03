# hp_legacy
An Appium automation framework for a legacy wifi optimization app that uses Pytest. 

* Prereqs (for Mac):
  * Python
    * Download: https://www.python.org/downloads/
  * PyCharm
    * Download: https://www.jetbrains.com/pycharm/download/?section=mac
  * Java
    * Download: https://www.oracle.com/java/technologies/downloads/
    * Add environment variables in your bash/zprofile:
      * `export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-11.jdk/Contents/Home`
      * `export PATH=$PATH:$JAVA_HOME/bin`
  * NodeJS
    * Download: https://nodejs.org/en/download
  * Android Studio
    * Download: https://developer.android.com/studio
    * Add Android SDK tools to your bash/zprofile:
      * `export ANDROID_HOME=/Users/<username>/Library/Android/sdk` 
      * `export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools`
  * Appium
    * `install -g appium@next`
    * `appium driver install xcuitest` (optional)
  * Appium Inspector
    * Download: https://github.com/appium/appium-inspector/releases