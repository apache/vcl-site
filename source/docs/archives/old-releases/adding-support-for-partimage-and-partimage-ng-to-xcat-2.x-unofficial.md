---
title: Adding support for partimage and partimage-ng to xCAT 2.x (unofficial)
---

<p>This is how I added support for partimage/partimage-ng to xCAT 2.x</p>

<h2><a name="Addingsupportforpartimageandpartimage-ngtoxCAT2.x%28unofficial%29-Overview"></a>Overview</h2>

<p>The method I used was based on a suggestion by Egan Ford.  I created an xCAT plugin to handle the imaging commands.  That plugin sets the node to boot a stateless image and configures a certain postscript to run that handles the image capture/restore.</p>

<h2><a name="Addingsupportforpartimageandpartimage-ngtoxCAT2.x%28unofficial%29-partimageng.pmxCATplugin"></a>partimageng.pm xCAT plugin</h2>

<p>First, I created an xCAT plugin to handle 2 nodeset commands for os type <b>image</b>: <em>install</em> and <em>image</em>.  This allows you to set the os type for a node to <b>image</b> and then run one of</p>
<div class="code panel" style="border-width: 1px;"><div class="codeContent panelContent">

<pre class="code-java">
nodeset &lt;node&gt; image
nodeset &lt;node&gt; install
</pre>
</div></div>
<p>which will cause an image of the node to be captured or installed the next time the node is booted.  The architecture for the node must always be set to x86 for this, but it will handle imaging/restoring both x86 and x86_64.</p>

<p>To use it, <a href="https://svn.apache.org/repos/asf/vcl/sandbox/xcat2partimageng/partimageng.pm" class="external-link" rel="nofollow">download</a> it from our SVN repository and put it in lib/perl/xCAT_plugin under your XCATROOT directory.</p>

<p>partimageng.pm requires a kickstart template file to be installed in your XCATROOT as share/xcat/install/image/default.tmpl. It should contain a single line with these contents:</p>
<div class="code panel" style="border-width: 1px;"><div class="codeContent panelContent">
<pre class="code-java">
#INCLUDE:../scripts/post.rh#
</pre>
</div></div>

<h2><a name="Addingsupportforpartimageandpartimage-ngtoxCAT2.x%28unofficial%29-partimagengpostscript"></a>partimageng postscript</h2>

<p>The partimageng.pm xCAT plugin configures the node to boot a stateless image and then to run the partimageng postscript.  This postscript handles the image capture/restore.  I did it all in a postscript to keep from having to rebuild the stateless image each time the capture/restore code needed to be modified.  The postscript can handle both partimage and partimage-ng formats. I initially only supported partimage-ng, but then realized that presented a compatibility problem where all of our previous images would have to be converted. There is a flag in the script to set which of the two applications gets used to create images that can be manually modified or passed in as a kernel parameter (I haven't set up a way for the partimageng.pm plugin to pass that kernel parameter yet though). Also, it determines what drive to image/install based on some stuff in /dev and /proc. The device can be specified as a kernel parameter, but again, this hasn't been added to the xCAT plugin. Right now, it only works with /dev/sda, /dev/sdb, /dev/hda, or /dev/hdb.</p>

<p><a href="https://svn.apache.org/repos/asf/vcl/sandbox/xcat2partimageng/partimageng" class="external-link" rel="nofollow">Download</a> it from our SVN repository and put it in your xCAT postscripts directory.</p>

<h2><a name="Addingsupportforpartimageandpartimage-ngtoxCAT2.x%28unofficial%29-listener.py"></a>listener.py</h2>

<p>This is a script I took from what was already part of xCAT that provides a way for xCAT's nodestat command to get the status of an install. I modified it to give the status of a partimage-ng or partimage install.</p>

<p>It needs to go in a directory I came up with to put the root image and required files. It is under your install path, for me, that is /install, so you need to put <a href="https://svn.apache.org/repos/asf/vcl/sandbox/xcat2partimageng/listener.py" class="external-link" rel="nofollow">listener.py</a> at /install/image/x86/installer_files</p>

<p>Also make sure to make listener.py executable:</p>
<div class="code panel" style="border-width: 1px;"><div class="codeContent panelContent">
<pre class="code-java">

chmod +x listener.py
</pre>
</div></div>

<h2><a name="Addingsupportforpartimageandpartimage-ngtoxCAT2.x%28unofficial%29-statelessimage"></a>stateless image</h2>

<p>This is the harder part. The images I have were built for IBM HS20, HS21, and HS22 blades. If you have other hardware, you may be able to use an existing kernel you have and update the kernel modules in the images I created. If that doesn't work, you'll need to create your own images. Since I don't have any notes on how I created them, I'll wait until someone needs help doing that to figure it out again (send a message to the vcl-user list). The short answer is to look at the xCAT docs on building a stateless image for your hardware. These images default to using eth0 as the installation NIC. To use a different NIC, set 'installnic' in the noderes table to the desired NIC. The root image contains the partimage and partimage-ng binaries.</p>

<p>There are three parts:</p>
<ul>
	<li><a href="http://people.apache.org/~jfthomps/partimageng_xCAT2x/vmlinuz" class="external-link" rel="nofollow">kernel - vmlinuz</a></li>
	<li><a href="http://people.apache.org/~jfthomps/partimageng_xCAT2x/initrd.img" class="external-link" rel="nofollow">initial RAM disk - initrd.img</a></li>

	<li><a href="http://people.apache.org/~jfthomps/partimageng_xCAT2x/rootimg.gz" class="external-link" rel="nofollow">root image - rootimg.gz</a></li>
</ul>


<p>Put vmlinuz and initrd.img at /tftpboot/xcat/image/x86.<br/>
Put rootimg.gz the same place you put the listener.py script (/install/image/x86/installer_files for me)</p>

<h2><a name="Addingsupportforpartimageandpartimage-ngtoxCAT2.x%28unofficial%29-ConfigurexCAT"></a>Configure xCAT</h2>

<p>The installer image uses NFS to mount the image store. In the past, it mounted the management node.  It has now been updated to be able to mount any NFS export available on the install network.  Two additional items need to be added to the xCAT site table:</p>

<ul>
	<li>IMAGELIBSERVER - this is the hostname or IP of the NFS server</li>
	<li>IMAGELIBINSTALLDIR - this is the directory being exported by the NFS server</li>
</ul>
