package main.controller;

import com.jfoenix.controls.JFXButton;
import javafx.animation.FadeTransition;
import javafx.animation.TranslateTransition;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.Pane;
import javafx.util.Duration;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import java.util.concurrent.TimeUnit;

public class HomeController implements Initializable {
    @FXML
    private Pane topPane, bottomPane, inputPane, outputPane;
    @FXML
    private ImageView animatedCircle, fixedCircle, img_mic;
    @FXML
    private JFXButton btn_stop, btn_animated;


    public void initialize(URL url, ResourceBundle rb) {
        btn_stop.setVisible(false);
    }

    public void fadeTransition(double transDuration, double startValue, double endValue, Pane paneObject){
        FadeTransition fade = new FadeTransition(Duration.seconds(transDuration));
        fade.setNode(paneObject);
        fade.setFromValue(startValue);
        fade.setToValue(endValue);
        fade.play();
    }

    public void moveTransition(double transDuration, double yCoordinate,Pane paneObject)
    {
        //Create new translate transition
        TranslateTransition transition = new TranslateTransition();
        transition.setDuration(Duration.seconds(transDuration));
        transition.setNode(paneObject);
        //Move in Y axis
        transition.setToY(yCoordinate);
        transition.play();
    }

    //set circle button animation
    public void setAnimation(boolean fixedState, boolean animatedState)
    {
        fixedCircle.setVisible(fixedState);
        animatedCircle.setVisible(animatedState);
    }

    @FXML
    void startMicrophone(MouseEvent event) throws IOException, InterruptedException {
        moveTransition(0.5, 455, topPane);
        fadeTransition(0.1, 1.0, 0.0, topPane);
        moveTransition(0.5, 455, bottomPane);
        fadeTransition(0.1, 1.0, 0.0, bottomPane);
        setAnimation(false, true);
        btn_stop.setVisible(true);
        btn_animated.setVisible(true);
        inputPane.setVisible(true);
        outputPane.setVisible(true);
        img_mic.setVisible(false);

        Runtime.getRuntime().exec("cmd /c taskkill /F /IM conhost.exe");
        // leave time to able to run second cmd command
        TimeUnit.MILLISECONDS.sleep(250);
        Runtime.getRuntime().exec("cmd /c start /MIN cmd.exe /c python src/main/takecommand.py");
        //waiting for loading model
        TimeUnit.MILLISECONDS.sleep(3500);
    }

    @FXML
    void stop_listen(MouseEvent event) throws IOException, InterruptedException {
        topPane.setTranslateY(0);
        bottomPane.setTranslateY(0);
        //return everything to normal home page without reloading
        //moveTransition(0.5, 0, topPane);
        fadeTransition(0.3, 0.0, 1.0, topPane);
        //(0.5, 0, bottomPane);
        fadeTransition(0.2, 0.0, 1.0, bottomPane);
        setAnimation(true, false);
        btn_stop.setVisible(false);
        btn_animated.setVisible(false);
        inputPane.setVisible(false);
        outputPane.setVisible(false);
        img_mic.setVisible(true);

        Runtime.getRuntime().exec("cmd /c taskkill /F /IM conhost.exe");
        // leave time to able to run second cmd command
        TimeUnit.MILLISECONDS.sleep(250);
        Runtime.getRuntime().exec("cmd /c start /MIN cmd.exe /c python src/main/wakeup.py");
    }
}
