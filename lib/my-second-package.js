'use babel';

import MySecondPackageView from './my-second-package-view';
import { CompositeDisposable } from 'atom';
var Promise = require('promise');

export default {

  mySecondPackageView: null,
  modalPanel: null,
  subscriptions: null,

  activate(state) {
    this.mySecondPackageView = new MySecondPackageView(state.mySecondPackageViewState);
    this.modalPanel = atom.workspace.addModalPanel({
      item: this.mySecondPackageView.getElement(),
      visible: false
    });
    // Events subscribed to in atom's system can be easily cleaned up with a CompositeDisposable
    this.subscriptions = new CompositeDisposable();

    // Register command that toggles this view
    atom.workspace.activePaneContainer.paneContainer.element.addEventListener("dblclick",this.toggle());
    this.subscriptions.add(atom.commands.add('atom-workspace', {
     'my-second-package:toggle': () => this.toggle()
    }));
  },

  deactivate() {
    console.log("Deactivate");
    this.modalPanel.destroy();
    this.subscriptions.dispose();
    this.mySecondPackageView.destroy();

  },

  serialize() {
    return {
      mySecondPackageViewState: this.mySecondPackageView.serialize()
    };
  },

  toggle() {
    mySecondPackageView = this.mySecondPackageView;
    modalPanel = this.modalPanel;
    tmp = "123";
    final_array = 0;
    console.log('MySecondPackage was toggled!');
    if(this.modalPanel.isVisible()){
      console.log("entered if");
      this.mySecondPackageView.empty_array();
      this.modalPanel.hide();
      this.deactivate();
    }
      console.log("Activate");
      const editor = atom.workspace.getActiveTextEditor();
      console.log(editor);
      console.log(editor.getSelectedText());
      var completeCode = editor.getText();
      // var cursorPosition = editor.getCursorBufferPosition();
      // var variableName = editor.getSelectedText();
      // var linesEncountered = 0;
      // var codeInjectPosition = 0;
      // for (var codeInjectPosition = 0; codeInjectPosition < completeCode.length; codeInjectPosition++) {
      //   if(completeCode.charAt(codeInjectPosition)=='\n'){
      //     linesEncountered++;
      //     if(linesEncountered == cursorPosition.row){
      //       break;
      //     }
      //   }
      // }
      // //console.log("the char is ");
      // var blank_spaces = 0
      // //console.log("the character");
      // //console.log(completeCode.charAt(codeInjectPosition));
      // codeInjectPosition++;
      // while(completeCode.charAt(codeInjectPosition)==" "){
      //   blank_spaces++;
      //   codeInjectPosition++;
      // }
      // console.log("blank spaces");
      // console.log(blank_spaces);
      // //while(completeCode.charAt(codeInjectPosition)!=";"){
      // //  codeInjectPosition++;
      // //}
      // while(completeCode.charAt(codeInjectPosition)!='\n'){
      //   codeInjectPosition++;
      // }
      // codeInjectPosition++;
      // //var spaces_encountered = 0;
      // //while(spaces_encountered<blank_spaces){
      // //  spaces_encountered++;
      // //  codeInjectPosition++;
      // //}
      //
      // var codeUptoArray = completeCode.slice(0,codeInjectPosition);
      // var codeAfterArray = completeCode.slice(codeInjectPosition,-1);
      // //console.log(codeUptoArray);
      // //console.log(codeAfterArray);

      const fs = require('fs');
      const path = require('path');
      const p = path.join(__dirname,'..','node_modules','node-powershell')
      const shell = require(p);

      var injectCode_python;
      //const injectionCode_CPP_path = editor.getPath();
      //console.log(injectionCode_CPP_path);
      const injectionCode_python_path = path.join(__dirname,'injectCodepython.txt');
      var read_python_path = path.join(__dirname,'read_python.txt');
      var webpage = path.join(__dirname,'html_new1.html');
      read_python_path = read_python_path.replace(/\\/gi,"\\\\");
      console.log(injectionCode_python_path);

      var injectCode_python = fs.readFileSync(injectionCode_python_path);
      combining_code(injectCode_python,step1);
      console.log("call has ended");
      var final_array;

      // function step1(){
      //   new Promise(function(resolve,reject){
      //
      //     console.log("powershell started");
      //     let ps = new shell({
      //     executionPolicy: 'Bypass',
      //     noProfile: true
      //     });
      //
      //     ps.addCommand('cd '+ __dirname)
      //     ps.addCommand('py python_output.py')
      //     ps.addCommand('exit')
      //     ps.invoke()
      //     .then(output => {
      //     console.log(output);
      //     })
      //     .catch(err => {
      //     ps.dispose();
      //     console.log(err);
      //     });
      //     //ps.dispose()
      //     //.then(function(){
      //     //  console.log("inside dispose");
      //     //  Start-Sleep -Milliseconds 10
      //     //  callback();
      //     //});
      //     console.log("powershell has ended");
      //     setTimeout(() => resolve("done!"), 2000);
      //
      //   }).then(function(result){window.open("file:///C:/Users/nax/.atom/packages/my-second-package/lib/html_new1.html")},function(error){window.open("file:///C:/Users/nax/.atom/packages/my-second-package/lib/html_new1.html")});
      // }
      function step1(){
        run_powershell(step2);
        console.log("exit step1");
      }
      function step2(){
        console.log("enter step2");
          get_array();
      }
      function step3(){
        run_functions()
      }



      function combining_code(injectCode_python,callback){
        injectCode_python = new TextDecoder("utf-8").decode(injectCode_python);

        injectCode_python = injectCode_python.replace(/<__b__s__>/gi,completeCode);
        // injectCode_python = injectCode_python.replace(/<__v__>/gi,variableName);
        // injectCode_python = injectCode_python.replace(/<__f__s__>/gi,read_python_path);
        //
        // injectCode_python = codeUptoArray + injectCode_python + "\n" + codeAfterArray;
        // //console.log("inject code");
        // //console.log(injectCode_python);
        // console.log("inject code 2");
        // console.log(injectCode_python);
        const fname = path.join(__dirname,'python_output.py');
        let data = injectCode_python;
        //console.log(data);
        fs.writeFileSync(fname, data,'utf-8');
        console.log("write file completed");
        callback();

      }

      function run_powershell(callback){

        console.log("powershell started");
        let ps = new shell({
        executionPolicy: 'Bypass',
        noProfile: true
        });

        ps.addCommand('cd '+ __dirname)
        // ps.addCommand('py python_output.py')
        // ps.addCommand('exit')
        ps.invoke()
          .then(output => {
            console.log("hello");
            let ps1 = new shell({
            executionPolicy: 'Bypass',
            noProfile: true
            });
            ps.addCommand('py python_output.py')
            ps.invoke()
            .then(output => {
              callback();
            })
            .catch(err => {
              console.log(err)
            })
            console.log(output)
          })
          .catch(err => {
          console.log(err);
        });


      //   new Promise(function(resolve,reject){
      //     resolve(ps.invoke()
      //     .then(output => {
      //       console.log(output)
      //       ps.dispose()
      //     })
      //     .catch(err => {
      //     console.log(err);
      //     ps.dispose()
      //   }));
      // }).then(function(result){console.log("entered resolve");});

        //ps.dispose()
        //.then(function(){
        //  console.log("inside dispose");
        //  Start-Sleep -Milliseconds 10
        //  callback();
        //});
        //callback();
        console.log("powershell has ended");

      }

      function get_array(){
        window.open(webpage)
        console.log("end")
      }

      // function run_functions(){
      //   console.log("in function");
      //   console.log(this.tmp);
      //   console.log("a;lsdklfj");
      //   console.log(this.tmp);
      //   this.mySecondPackageView.display_array(final_array);
      //   this.modalPanel.show();
      // }

      //for (var k = codeInjectPosition; k < codeInjectPosition+10; k++){
      //  alert(completeCode.charAt(k) + k + " " + cursorPosition.row);
      //}


      //console.log("inject code 2");
      //console.log(injectCode_python);
      //const fname = path.join(__dirname,'Output.txt');
      //let data = injectCode_python;
      //console.log(data);
      //fs.writeFile(fname, data, (err) => {
      //  if (err) throw err;
        //console.log(__dirname)
        //console.log("file is made");
      //});


  }

};
