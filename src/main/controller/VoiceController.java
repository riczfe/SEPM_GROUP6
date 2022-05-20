package main.controller;

import com.jfoenix.controls.JFXButton;
import com.jfoenix.controls.JFXComboBox;
import com.jfoenix.controls.JFXToggleButton;
import javafx.animation.FadeTransition;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.Pane;
import javafx.stage.Modality;
import javafx.stage.Stage;
import javafx.stage.StageStyle;
import javafx.util.Duration;

import java.awt.*;
import java.io.*;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.Properties;
import java.util.ResourceBundle;
import java.util.concurrent.TimeUnit;

public class VoiceController implements Initializable {
    String[] langs = {"Default", "English (United States)"};
    String[] langs_setting = {"default", "en_us"};
    @FXML
    private JFXToggleButton toggleVoiceControl;
    @FXML
    private JFXComboBox<String> inputComboBox, outputComboBox;
    @FXML
    private JFXButton btn_cancel, btn_save;
    @FXML
    private ImageView infoIcon;
    @FXML
    private Pane infoBox, rulesBox;

    public void initialize(URL url, ResourceBundle rb) {
        onStartUp();
    }

    public void onStartUp(){
        //add language data to comboBox
        ObservableList<String> options = FXCollections.observableArrayList();
        for (int i=0; i< langs.length; i++)
        {
            options.add(langs[i]);
        }
        inputComboBox.setItems(options);
        outputComboBox.setItems(options);

        //listener for function combobox
        comboBoxListener(inputComboBox);
        comboBoxListener(outputComboBox);

        //listener for toggle button
        toggleListener(toggleVoiceControl);

        //hover on ? icon
        iconHoverEffect(infoIcon, infoBox);

        loadSettings();

        //disable save and cancel button
        btn_cancel.setDisable(true);
        btn_save.setDisable(true);
    }

    public void comboBoxListener(JFXComboBox comboBox){
        //listener for function combobox
        comboBox.showingProperty().addListener((obs, oldItem, newItem) -> {
            if (!newItem)
            {
                //System.out.println(comboBox.getValue());
                btn_cancel.setDisable(false);
                btn_save.setDisable(false);
            }
        });
    }

    public void toggleListener(JFXToggleButton toggleButton){
        //listener for function combobox
        toggleButton.selectedProperty().addListener((obs, oldItem, newItem) -> {
            if (!newItem) {
                try {
                    //System.out.println("off");
                    Runtime.getRuntime().exec("cmd /c taskkill /F /IM conhost.exe");
                    // leave time to able to run second cmd command
                    TimeUnit.MILLISECONDS.sleep(250);
                    Runtime.getRuntime().exec("cmd /c start /MIN cmd.exe /c python src/main/wakeup.py");
                    Runtime.getRuntime().exec("taskkill /f /im sapisvr.exe");
                } catch (IOException | InterruptedException e) {
                    e.printStackTrace();
                }
            }
            else {
                try {
                    Runtime.getRuntime().exec("cmd /c taskkill /F /IM conhost.exe");
                    // leave time to able to run second cmd command
                    TimeUnit.MILLISECONDS.sleep(250);
                    Runtime.getRuntime().exec("cmd /c start /MIN cmd.exe /K python src/main/control.py");
                } catch (IOException | InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });
    }

    //load setting in properties
    public void loadSettings(){
        Properties prop = new Properties();
        String filename = "./src/main/config/settings.properties";
        try (InputStream input = new FileInputStream(filename)){
            if (input == null) {
                //System.out.println("Sorry, unable to find config.properties");
                return;
            }

            //load a properties file from class path, inside static method
            prop.load(input);

            //get the property value and call settingApp function
            settingApp(prop.getProperty("agree_sr"), prop.getProperty("input_lang"), prop.getProperty("app_lang"));
        }
        catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    //setting the application based on settings.properties
    public void settingApp(String agree_sr, String input_lang, String app_lang){
        switch(agree_sr){
            case "false":
            {
                rulesBox.setVisible(true);
                toggleVoiceControl.setDisable(true);
                inputComboBox.setDisable(true);
                outputComboBox.setDisable(true);
                break;
            }
            case "true":
            {
                rulesBox.setVisible(false);
                toggleVoiceControl.setDisable(false);
                inputComboBox.setDisable(false);
                outputComboBox.setDisable(false);
                break;
            }
            default:
            {
                agree_sr = "false";
                //System.out.print("Cannot find rule system settings, switching to default.");
                rulesBox.setVisible(true);
                toggleVoiceControl.setDisable(true);
                inputComboBox.setDisable(true);
                outputComboBox.setDisable(true);
                break;
            }
        }

        switch(input_lang) {
            case "default":
                inputComboBox.setValue(langs[0]);
                break;
            case "en_us":
                inputComboBox.setValue(langs[1]);
                break;
            default:
                //System.out.println("Cannot find input language system settings, switching to default.");
                inputComboBox.setValue(langs[0]);
                input_lang = "default";
                break;
        }

        switch(app_lang) {
            case "default":
                outputComboBox.setValue(langs[0]);
                break;
            case "en_us":
                outputComboBox.setValue(langs[1]);
                break;
            default:
                //System.out.println("Cannot find app language system settings, switching to default");
                outputComboBox.setValue(langs[0]);
                app_lang = "default";
                break;
        }

        writeSettings(agree_sr, input_lang, app_lang);
    }

    public void writeSettings(String value1, String value2, String value3) {
        Properties prop = new Properties();
        String filename = "./src/main/config/settings.properties";
        try (OutputStream output = new FileOutputStream(filename)) {

            // set the properties value
            prop.setProperty("agree_sr", value1);
            prop.setProperty("input_lang", value2);
            prop.setProperty("app_lang", value3);

            // save properties to project root folder
            prop.store(output, null);

            //System.out.println(prop);

        } catch (IOException io) {
            io.printStackTrace();
        }
    }
    
    public void iconHoverEffect(javafx.scene.image.ImageView icon, Pane box)
    {
        FadeTransition fadeIn = new FadeTransition(Duration.seconds(0.5));
        //? icon effect
        icon.hoverProperty().addListener((observable, oldValue, newValue) -> {
            if (newValue)
            {
                box.setVisible(true);
                fadeIn.setNode(box);
                fadeIn.setFromValue(0.0);
                fadeIn.setToValue(1.0);
                fadeIn.playFromStart();
            }
            else
            {
                box.setVisible(false);
            }
        });
    }

    public void openNotification(MouseEvent event) throws IOException{
        Stage stage = new Stage();
        Parent root = FXMLLoader.load(getClass().getResource("/main/ui/Notification.fxml"));
        stage.setScene(new Scene(root));
        stage.initModality(Modality.WINDOW_MODAL);
        stage.initStyle(StageStyle.UNDECORATED);
        stage.initOwner(((Node)event.getSource()).getScene().getWindow() );
        stage.show();

        stage.setOnHidden(we -> onStartUp());
    }

    @FXML
    public void showCommands(MouseEvent event) throws IOException, URISyntaxException {
        Desktop.getDesktop().browse(new URI("https://github.com/riczfe/SEPM_GROUP6"));
    }

    //save button
    //write new settings.properties.
    @FXML
    public void save(MouseEvent event) {
        String input_lang="";
        String app_lang = "";
        for (int i=0;i<langs.length;i++)
        {
            if (inputComboBox.getSelectionModel().getSelectedItem().equals(langs[i]))
            {
                input_lang = langs_setting[i];
            }

            if (outputComboBox.getSelectionModel().getSelectedItem().equals(langs[i]))
            {
                app_lang = langs_setting[i];
            }
        }

        writeSettings("true", input_lang, app_lang);
        btn_cancel.setDisable(true);
        btn_save.setDisable(true);
    }

    //cancel button
    //reload settings.properties
    @FXML
    public void cancel(MouseEvent event) {
        loadSettings();
        btn_cancel.setDisable(true);
        btn_save.setDisable(true);
    }
}
