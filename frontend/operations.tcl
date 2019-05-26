#############################################################################
# Generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#  May 19, 2019 02:59:09 PM IST  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family Consolas -size 14 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font11
vTcl:font:add_font \
    "-family Consolas -size 12 -weight normal -slant roman -underline 1 -overstrike 0" \
    user \
    vTcl:font13
vTcl:font:add_font \
    "-family {Segoe UI} -size 12 -weight normal -slant italic -underline 0 -overstrike 0" \
    user \
    vTcl:font15
vTcl:font:add_font \
    "-family Consolas -size 12 -weight bold -slant italic -underline 0 -overstrike 0" \
    user \
    vTcl:font19
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#ffaa00} 
    wm focusmodel $top passive
    wm geometry $top 900x522+201+100
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1370 749
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Operations"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    frame $top.fra43 \
        -borderwidth 2 -background {#ffffff} -height 455 -width 825 
    vTcl:DefineAlias "$top.fra43" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra43
    message $site_3_0.mes45 \
        -background {#ffffff} \
        -font {-family {Consolas} -size 14 -weight bold} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Operations -->} -width 150 
    vTcl:DefineAlias "$site_3_0.mes45" "Message1" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes46 \
        -background {#ffffff} \
        -font {-family {Consolas} -size 12 -weight bold -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black \
        -text {CLICK on OPERATION as your wish on default file (data.txt)} \
        -width 540 
    vTcl:DefineAlias "$site_3_0.mes46" "Message2" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but47 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#e5ffc7} -disabledforeground {#a3a3a3} \
        -font {-family {Segoe UI} -size 12 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -relief flat -text {Show Data} 
    vTcl:DefineAlias "$site_3_0.but47" "Button1" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes54 \
        -background {#ffffff} \
        -font {-family {Consolas} -size 12 -underline 1} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black \
        -text ----------------------------------------------------------------------------------- \
        -width 760 
    vTcl:DefineAlias "$site_3_0.mes54" "Message3" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but55 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#e5ffc7} -disabledforeground {#a3a3a3} \
        -font {-family {Segoe UI} -size 12 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -relief flat -text {Load Data to Tree} 
    vTcl:DefineAlias "$site_3_0.but55" "Button2" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but56 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#e5ffc7} -disabledforeground {#a3a3a3} \
        -font {-family {Segoe UI} -size 12 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -relief flat -text {Search a Record} 
    vTcl:DefineAlias "$site_3_0.but56" "Button3" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but57 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#88ff00} -disabledforeground {#a3a3a3} \
        -font {-family {Segoe UI} -size 12 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -relief flat -text {Add New Record} 
    vTcl:DefineAlias "$site_3_0.but57" "Button4" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but58 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#78dbff} -disabledforeground {#a3a3a3} \
        -font {-family {Segoe UI} -size 12 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -relief flat -text {Modify a Record} 
    vTcl:DefineAlias "$site_3_0.but58" "Button5" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but59 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#ff7d7d} -disabledforeground {#a3a3a3} \
        -font {-family {Segoe UI} -size 12 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -relief flat -text {Delete a Record} 
    vTcl:DefineAlias "$site_3_0.but59" "Button6" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but60 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#e5ffc7} -disabledforeground {#a3a3a3} \
        -font {-family {Segoe UI} -size 12 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -relief flat -text {Goto Index Page} 
    vTcl:DefineAlias "$site_3_0.but60" "Button7" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.mes45 \
        -in $site_3_0 -x 330 -y 20 -width 150 -relwidth 0 -height 33 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes46 \
        -in $site_3_0 -x 20 -y 60 -width 540 -relwidth 0 -height 33 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but47 \
        -in $site_3_0 -x 90 -y 140 -width 157 -relwidth 0 -height 64 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes54 \
        -in $site_3_0 -x 30 -y 360 -width 760 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but55 \
        -in $site_3_0 -x 330 -y 140 -width 157 -height 64 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but56 \
        -in $site_3_0 -x 570 -y 140 -width 157 -height 64 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but57 \
        -in $site_3_0 -x 90 -y 250 -width 157 -height 64 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but58 \
        -in $site_3_0 -x 330 -y 250 -width 157 -height 64 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but59 \
        -in $site_3_0 -x 570 -y 250 -width 157 -height 64 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but60 \
        -in $site_3_0 -x 650 -y 400 -width 137 -relwidth 0 -height 34 \
        -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra43 \
        -in $top -x 40 -y 30 -width 825 -relwidth 0 -height 455 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
