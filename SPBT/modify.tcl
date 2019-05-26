#############################################################################
# Generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#  May 21, 2019 02:59:14 AM IST  platform: Windows NT
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
    "-family Consolas -size 12 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font10
vTcl:font:add_font \
    "-family Consolas -size 13 -weight normal -slant italic -underline 0 -overstrike 0" \
    user \
    vTcl:font11
vTcl:font:add_font \
    "-family Consolas -size 11 -weight normal -slant italic -underline 0 -overstrike 0" \
    user \
    vTcl:font13
vTcl:font:add_font \
    "-family Consolas -size 13 -weight normal -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font14
vTcl:font:add_font \
    "-family Consolas -size 13 -weight bold -slant italic -underline 0 -overstrike 0" \
    user \
    vTcl:font15
vTcl:font:add_font \
    "-family Consolas -size 13 -weight bold -slant italic -underline 1 -overstrike 0" \
    user \
    vTcl:font9
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
    wm geometry $top 900x500+165+126
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
    wm title $top "Modify Record"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    frame $top.fra43 \
        -borderwidth 2 -background {#ffffff} -height 445 -width 845 
    vTcl:DefineAlias "$top.fra43" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra43
    message $site_3_0.mes44 \
        -background {#ffffff} \
        -font {-family {Consolas} -size 13 -weight bold -slant italic -underline 1} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Modify Record} -width 200 
    vTcl:DefineAlias "$site_3_0.mes44" "Message1" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes45 \
        -background {#08f900} \
        -font {-family {Consolas} -size 12 -weight bold} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text Modified -width 160 
    vTcl:DefineAlias "$site_3_0.mes45" "Message2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab46 \
        -anchor e -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13 -weight bold -slant italic} \
        -foreground {#000000} -text {Enter User ID to Modify that Record} 
    vTcl:DefineAlias "$site_3_0.lab46" "Label1" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but47 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#63fff5} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -relief flat -text {Get Form} 
    vTcl:DefineAlias "$site_3_0.but47" "Button1" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent48 \
        -background {#fffce0} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13} -foreground {#000000} \
        -insertbackground black -relief groove 
    vTcl:DefineAlias "$site_3_0.ent48" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab49 \
        -anchor e -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 11 -slant italic} \
        -foreground {#000000} -text {Emp ID} 
    vTcl:DefineAlias "$site_3_0.lab49" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab51 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 11 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Name Prefix} 
    vTcl:DefineAlias "$site_3_0.lab51" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab55 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 11 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {First Name} 
    vTcl:DefineAlias "$site_3_0.lab55" "Label4" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab56 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 11 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Middle Initial} 
    vTcl:DefineAlias "$site_3_0.lab56" "Label5" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab57 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 11 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Last Name} 
    vTcl:DefineAlias "$site_3_0.lab57" "Label6" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab59 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 11 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text Gender 
    vTcl:DefineAlias "$site_3_0.lab59" "Label7" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab60 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 11 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {E Mail} 
    vTcl:DefineAlias "$site_3_0.lab60" "Label8" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab61 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 11 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Father's Name} 
    vTcl:DefineAlias "$site_3_0.lab61" "Label9" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab62 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 11 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Mother's Name} 
    vTcl:DefineAlias "$site_3_0.lab62" "Label10" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab63 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 11 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Age in Yrs} 
    vTcl:DefineAlias "$site_3_0.lab63" "Label11" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent64 \
        -background {#fffce0} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief groove -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent64" "Entry2" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent65 \
        -background {#fffce0} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief groove -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent65" "Entry3" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent66 \
        -background {#fffce0} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief groove -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent66" "Entry4" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent67 \
        -background {#fffce0} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief groove -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent67" "Entry5" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent68 \
        -background {#fffce0} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief groove -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent68" "Entry6" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent69 \
        -background {#fffce0} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief groove -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent69" "Entry7" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent70 \
        -background {#fffce0} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief groove -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent70" "Entry8" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent71 \
        -background {#fffce0} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief groove -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent71" "Entry9" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent72 \
        -background {#fffce0} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief groove -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent72" "Entry10" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent73 \
        -background {#fffce0} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief groove -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent73" "Entry11" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab75 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 11 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Date of Joining} 
    vTcl:DefineAlias "$site_3_0.lab75" "Label12" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent76 \
        -background {#fffce0} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief groove -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent76" "Entry12" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab77 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 11 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Age in Company (Years)} 
    vTcl:DefineAlias "$site_3_0.lab77" "Label13" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab78 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 11 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text Salary 
    vTcl:DefineAlias "$site_3_0.lab78" "Label14" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab79 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 11 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text SSN 
    vTcl:DefineAlias "$site_3_0.lab79" "Label15" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab80 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 11 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Phone No} 
    vTcl:DefineAlias "$site_3_0.lab80" "Label16" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab81 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 11 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text City 
    vTcl:DefineAlias "$site_3_0.lab81" "Label17" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab82 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 11 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text State 
    vTcl:DefineAlias "$site_3_0.lab82" "Label18" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab83 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 11 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text Zip 
    vTcl:DefineAlias "$site_3_0.lab83" "Label19" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent84 \
        -background {#fffce0} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief groove -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent84" "Entry13" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent85 \
        -background {#fffce0} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief groove -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent85" "Entry14" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent86 \
        -background {#fffce0} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief groove -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent86" "Entry15" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent87 \
        -background {#fffce0} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief groove -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent87" "Entry16" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent88 \
        -background {#fffce0} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief groove -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent88" "Entry17" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent89 \
        -background {#fffce0} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief groove -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent89" "Entry18" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent90 \
        -background {#fffce0} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief groove -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent90" "Entry20" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but91 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#63fff5} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -relief flat -text {Go Back} 
    vTcl:DefineAlias "$site_3_0.but91" "Button1_42" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but92 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#63fff5} -disabledforeground {#a3a3a3} \
        -font {-family {Consolas} -size 13 -slant italic} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -relief flat -text Modify 
    vTcl:DefineAlias "$site_3_0.but92" "Button1_43" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.mes44 \
        -in $site_3_0 -x 310 -y 20 -width 200 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes45 \
        -in $site_3_0 -x 630 -y 20 -width 160 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab46 \
        -in $site_3_0 -x 30 -y 60 -width 324 -relwidth 0 -height 31 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but47 \
        -in $site_3_0 -x 610 -y 60 -width 147 -relwidth 0 -height 34 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent48 \
        -in $site_3_0 -x 380 -y 60 -width 194 -relwidth 0 -height 30 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab49 \
        -in $site_3_0 -x 20 -y 120 -width 164 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab51 \
        -in $site_3_0 -x 20 -y 150 -width 164 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab55 \
        -in $site_3_0 -x 20 -y 180 -width 164 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab56 \
        -in $site_3_0 -x 20 -y 210 -width 164 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab57 \
        -in $site_3_0 -x 20 -y 240 -width 164 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab59 \
        -in $site_3_0 -x 20 -y 270 -width 164 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab60 \
        -in $site_3_0 -x 20 -y 300 -width 164 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab61 \
        -in $site_3_0 -x 20 -y 330 -width 164 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab62 \
        -in $site_3_0 -x 20 -y 360 -width 164 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab63 \
        -in $site_3_0 -x 20 -y 390 -width 164 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent64 \
        -in $site_3_0 -x 210 -y 110 -width 154 -relwidth 0 -height 30 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent65 \
        -in $site_3_0 -x 210 -y 140 -width 154 -height 30 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent66 \
        -in $site_3_0 -x 210 -y 170 -width 154 -height 30 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent67 \
        -in $site_3_0 -x 210 -y 200 -width 154 -height 30 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent68 \
        -in $site_3_0 -x 210 -y 230 -width 154 -height 30 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent69 \
        -in $site_3_0 -x 210 -y 260 -width 154 -height 30 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent70 \
        -in $site_3_0 -x 210 -y 290 -width 154 -height 30 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent71 \
        -in $site_3_0 -x 210 -y 320 -width 154 -height 30 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent72 \
        -in $site_3_0 -x 210 -y 350 -width 154 -height 30 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent73 \
        -in $site_3_0 -x 210 -y 380 -width 154 -height 30 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab75 \
        -in $site_3_0 -x 400 -y 120 -width 184 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent76 \
        -in $site_3_0 -x 610 -y 110 -width 154 -height 30 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab77 \
        -in $site_3_0 -x 400 -y 150 -width 184 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab78 \
        -in $site_3_0 -x 400 -y 180 -width 184 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab79 \
        -in $site_3_0 -x 400 -y 210 -width 184 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab80 \
        -in $site_3_0 -x 400 -y 240 -width 184 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab81 \
        -in $site_3_0 -x 400 -y 270 -width 184 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab82 \
        -in $site_3_0 -x 400 -y 300 -width 184 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab83 \
        -in $site_3_0 -x 400 -y 330 -width 184 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent84 \
        -in $site_3_0 -x 610 -y 140 -width 154 -height 30 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent85 \
        -in $site_3_0 -x 610 -y 170 -width 154 -height 30 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent86 \
        -in $site_3_0 -x 610 -y 200 -width 154 -height 30 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent87 \
        -in $site_3_0 -x 610 -y 230 -width 154 -height 30 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent88 \
        -in $site_3_0 -x 610 -y 260 -width 154 -height 30 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent89 \
        -in $site_3_0 -x 610 -y 290 -width 154 -height 30 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent90 \
        -in $site_3_0 -x 610 -y 320 -width 154 -height 30 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but91 \
        -in $site_3_0 -x 490 -y 380 -width 107 -relwidth 0 -height 34 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but92 \
        -in $site_3_0 -x 620 -y 380 -width 147 -height 34 -anchor nw \
        -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra43 \
        -in $top -x 30 -y 30 -width 845 -relwidth 0 -height 445 -relheight 0 \
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
