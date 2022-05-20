package main.controller;

import com.jfoenix.controls.JFXButton;
import com.jfoenix.controls.JFXCheckBox;
import javafx.beans.value.ObservableValue;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.input.MouseEvent;
import javafx.stage.Stage;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.URL;
import java.util.Properties;
import java.util.ResourceBundle;

public class NotificationController implements Initializable {
    @FXML
    private JFXButton btn_accept, btn_decline;
    @FXML
    private JFXCheckBox agreeCheckBox;

    boolean agreeCheckBoxSelected;

    public void initialize(URL url, ResourceBundle rb){
        agreeCheckBox.selectedProperty().addListener(
                (ObservableValue<? extends Boolean> ov, Boolean old_val, Boolean new_val) ->
                {
                    agreeCheckBoxSelected = agreeCheckBox.isSelected();
                    if (agreeCheckBoxSelected)
                    {
                        btn_accept.setDisable(false);
                    }
                    else
                    {
                        btn_accept.setDisable(true);
                    }
                });
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

            System.out.println(prop);

        } catch (IOException io) {
            io.printStackTrace();
        }
    }

    @FXML
    void agree_close(MouseEvent event) {
        writeSettings("true", "default", "default");
        Node source = (Node) event.getSource();
        Stage stage  = (Stage) source.getScene().getWindow();
        stage.close();
    }

    @FXML
    void decline_close(MouseEvent event) {
        Node source = (Node) event.getSource();
        Stage stage  = (Stage) source.getScene().getWindow();
        stage.close();
    }
}
