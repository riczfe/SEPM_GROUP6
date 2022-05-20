package main;

import com.dustinredmond.fxtrayicon.FXTrayIcon;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.stage.Stage;
import javafx.stage.StageStyle;
import java.io.IOException;

public class Main extends Application
{
    double x,y = 0;
    public static Stage getStage;
    @Override
    public void start(Stage primaryStage) throws Exception
    {
        getStage = primaryStage;
        Parent root = FXMLLoader.load(getClass().getResource("ui/MainUI.fxml"));

        primaryStage.initStyle(StageStyle.UNDECORATED);
        primaryStage.initStyle(StageStyle.TRANSPARENT);


        root.setOnMousePressed(event -> {
            x = event.getSceneX();
            y = event.getSceneY();
        });

        root.setOnMouseDragged(event -> {
            primaryStage.setX(event.getScreenX() - x);
            primaryStage.setY(event.getScreenY() - y);
        });

        FXTrayIcon trayIcon = new FXTrayIcon(primaryStage, getClass().getResource("icon_small.png"));
        trayIcon.show();
        trayIcon.showMessage("Julee", "Your best virtual assistant.");

        Scene scene = new Scene(root);
        scene.setFill(javafx.scene.paint.Color.TRANSPARENT);
        primaryStage.setScene(scene);
        primaryStage.show();
        primaryStage.setTitle("Julee");
        Image image = new Image("main/icon.png");
        primaryStage.getIcons().add(image);

        primaryStage.setAlwaysOnTop(true);

        //run py
        try {
            Runtime.getRuntime().exec("cmd /c start /MIN cmd.exe /c python src/main/wakeup.py");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args)
    {
        launch(args);
    }
}
