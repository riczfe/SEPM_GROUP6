package main.controller;

import de.jensd.fx.glyphs.fontawesome.FontAwesomeIconView;
import javafx.animation.FadeTransition;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.Pane;
import javafx.util.Duration;
import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import java.util.concurrent.TimeUnit;

public class MainUIController implements Initializable {

    int homeCount, voiceCount, aboutCount = 0;

    @Override
    public void initialize(URL url, ResourceBundle rb){
        voiceCount = aboutCount = 0;
        homeCount++;
        if ((homeCount % 2) == 1)
        {
            homeTri.setVisible(true);
            voice_Tri.setVisible(false);
            about_Tri.setVisible(false);
            String path = "/main/ui/Home.fxml";
            try {
                appearTransition(path);
            }
            catch (IOException e) {
                e.printStackTrace();
            }
        }
        else
        {
            homeTri.setVisible(false);
            disappearTransition();
        }
    }

    @FXML
    private FontAwesomeIconView homeTri;
    @FXML
    private FontAwesomeIconView voice_Tri;
    @FXML
    private FontAwesomeIconView about_Tri;
    @FXML
    private Pane pane;

    //for fade transition
    private FadeTransition fade = new FadeTransition(Duration.seconds(0.3));

    public void appearTransition(String path) throws IOException {
        pane.getChildren().removeAll();
        pane.getChildren().setAll();
        Parent fxml = FXMLLoader.load(getClass().getResource(path));
        fade.setNode(pane);
        fade.setFromValue(0.0);
        fade.setToValue(1.0);
        fade.playFromStart();
        pane.getChildren().removeAll();
        pane.getChildren().setAll(fxml);
    }

    public void disappearTransition(){
        fade.setNode(pane);
        fade.setFromValue(1.0);
        fade.setToValue(0.0);
        fade.play();
    }

    @FXML
    void open_about(MouseEvent event) throws IOException
    {
        voiceCount = homeCount = 0;
        aboutCount++;
        if ((aboutCount % 2) == 1)
        {
            homeTri.setVisible(false);
            voice_Tri.setVisible(false);
            about_Tri.setVisible(true);
            String path = "/main/ui/About.fxml";
            appearTransition(path);
        }
        else
        {
            about_Tri.setVisible(false);
            disappearTransition();
        }
    }

    @FXML
    void open_exit(MouseEvent event) throws IOException, InterruptedException {
        TimeUnit.MILLISECONDS.sleep(250);
        Runtime.getRuntime().exec("taskkill /f /im sapisvr.exe");
        TimeUnit.MILLISECONDS.sleep(250);
        Runtime.getRuntime().exec("cmd /c taskkill /F /IM conhost.exe");
        System.exit(0);

        /*
        Minimize to taskbar
        Stage stage= (Stage) ((Node) event.getSource()).getScene().getWindow();
        stage.close();
         */
    }

    @FXML
    void open_home(MouseEvent event) throws IOException {
        voiceCount = aboutCount = 0;
        homeCount++;
        if ((homeCount % 2) == 1)
        {
            homeTri.setVisible(true);
            voice_Tri.setVisible(false);
            about_Tri.setVisible(false);
            String path = "/main/ui/Home.fxml";
            appearTransition(path);
        }
        else
        {
            homeTri.setVisible(false);
            disappearTransition();
        }
    }

    @FXML
    void open_voice_control(MouseEvent event) throws IOException {
        homeCount = aboutCount = 0;
        voiceCount++;
        if ((voiceCount % 2) == 1)
        {
            homeTri.setVisible(false);
            voice_Tri.setVisible(true);
            about_Tri.setVisible(false);
            String path = "/main/ui/VoiceControl.fxml";
            appearTransition(path);
        }
        else
        {
            voice_Tri.setVisible(false);
            disappearTransition();
        }
    }
}
